# -*- coding: utf-8 -*-

import MySQLdb as mySQL
import datetime
import time

""" global MySQL settings """
mysql_user_name = ''
mysql_password = ''
mysql_ip = '127.0.0.1'
mysql_db = 'binpacking_fast'

def checkCapacity(articles, bin_contents, bin_cap):
    """ articles: a dictionary of the items to be loaded into the bins: the key is the article id and the value is the article volume """
    """ bin_contents is expected to be a list of lists, where each sub-list is the contents of each bin vis article ids  """
    """ bin_cap: capacity of each of the identical bins """
    """ This function returns two parameters, the first of which is the number of bins that are within capacity and, the second, the number of overloaded bins """
    
    num_ok = 0
    num_over = 0
    if isinstance(articles,dict):
        if isinstance(bin_contents,list):
            item_key_good = True
            for this_bin in bin_contents:
                if isinstance(this_bin,list):
                    load = 0.0
                    for this_item in this_bin:
                        if this_item not in items.keys():
                            item_key_good = False
                        else:
                            load += articles[this_item]
                    if item_key_good == False:
                        print "function checkCapacity(), bad item key"
                        return 'bad_key', 'bad_key'
                    elif load <= bin_cap:
                        num_ok += 1
                    else:
                        num_over += 1
                else:
                    print "function checkCapacity(),contents of each bin must be in a sub-list"
                    return 'sublist_error','sublist_error'
            return num_ok, num_over
        else:
            print "function checkCapacity(), bin_contents must be in a list"
            return 'list_needed', 'list_needed'
    else:
        print "function checkCapacity(), articles argument requires a dictionary"
        return 'dict_needed', 'dict_needed'
        
def checkAllPoints(articles, bin_contents):
    """ Check to be sure that all items are packed in one bin """
    
    err_mess = ""
    err_mult= False
    checkit = {}
    for this_bin in bin_contents:
        for this_art in this_bin:
            checkit[this_art] = checkit.get(this_art,0) + 1
            if checkit[this_art] > 1:
                err_mult = True
                err_mess += "Loc assigned mult times"
                
    err_all = False
    for key_art in articles.keys():
        if key_art not in checkit.keys():
            err_all = True
            err_mess += "Some locs not assigned to bins"
            
    return err_mult, err_all, err_mess

def binpack(articles,bin_cap):
    article_items=articles.items()
    article_items_sorted=sorted(article_items,key=lambda x:x[1],reverse=True)
    
    list_bins = []
    my_bin=[]
    my_team_number_or_name = "jdeng01"
    
    for key,weight in article_items_sorted:
            alloc_flag = False
            for my_bin in list_bins:
                alternates=my_bin[0::2]
                if sum(my_bin) + weight-sum(alternates) <= bin_cap:
                        my_bin.extend((key,weight))
                        alloc_flag=True
                        break
                        
            if alloc_flag == False:
                newBin = []
                newBin.extend((key,weight))
                list_bins.append(newBin)
                
    for i in range(len(list_bins)):         
        del list_bins[i][1::2]
    bin_contents=list_bins
            
    return my_team_number_or_name, bin_contents       # use this return statement when you have items to load in the knapsack

def getDBDataList(commandString):
    #cnx = mySQL.connect(user=mysql_user_name, passwd=mysql_password,
    #                    host=mysql_ip, db=mysql_db)
                        
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute(commandString)
    items = []
    for item in list(cursor):
        items.append(item[0])
    cursor.close()
    cnx.close()
    return items
   
"""
def putResultsData(insertList, connection):
    cursor = connection.cursor()
    cursor.executemany("CALL spPutResultsData(%s,%s,%s)", insertList)
    connection.commit()
    cursor.close()
"""
    
""" db_get_data connects with the database and returns a dictionary with the knapsack items """
def db_get_data(problem_id):
    #cnx = mySQL.connect(user=mysql_user_name, passwd=mysql_password,
    #                    host=mysql_ip, db=mysql_db)
    cnx = db_connect()
                        
    cursor = cnx.cursor()
    cursor.execute("CALL spGetBinpackCap(%s);" % problem_id)
    bin_cap = cursor.fetchall()[0][0]
    cursor.close()
    cursor = cnx.cursor()
    cursor.execute("CALL spGetBinpackData(%s);" % problem_id)
    items = {}
    blank = cursor.fetchall()
    for row in blank:
        items[row[0]] = row[1]
    cursor.close()
    cnx.close()
    return bin_cap, items
    
def db_insert_results(problem_id,participant,result):
    #cnx = mySQL.connect(user=mysql_user_name, passwd=mysql_password,
    #                    host=mysql_ip, db=mysql_db)
    cnx = db_connect()                       
    cursor = cnx.cursor()
    cursor.execute("CALL spInsertResults(%s, %s, %s);" , (problem_id,participant,result))
    cursor.close()
    cnx.commit()
    cnx.close
    
def db_connect():
    cnx = mySQL.connect(user=mysql_user_name, passwd=mysql_password,
                        host=mysql_ip, db=mysql_db)
    return cnx
    
    
    
""" Get solutions based on submission """
problems = getDBDataList('CALL spGetProblemIds();') 
silent_mode = False    # use this variable to turn on/off appropriate messaging depending on student or instructor use
filename_post = 'leaderboard.html'

for problem_id in problems:
    bin_cap, items = db_get_data(problem_id)
    #finished = False
    errors = False
    response = None
    
    #while finished == False:
    startTime = time.time()
    team_num, response = binpack(items,bin_cap)
    execTime = time.time() - startTime
    h = int(execTime/3600)
    m = int(execTime - h *3600)/60
    s = execTime - 3600 * h - 60 * m
    myTime = '{:02d}'.format(h) + ':' + '{:02d}'.format(m) + ':' + '{:07.4f}'.format(s)
            
    #if not isinstance(response,str):
    if isinstance(response,list):
        num_ok, num_over = checkCapacity(items, response, bin_cap)
        if not isinstance(num_ok,int) or not isinstance(num_over,int):
            errors = True
            if silent_mode:
                status = num_ok
            else:
                print "P"+str(problem_id)+num_ok+"_"
                
        err_mult, err_all, err_mess = checkAllPoints(items, response)
        if err_mult or err_all:
            errors = True
            if silent_mode:
                status += "_" + err_mess
            else:
                print "P"+str(problem_id)+err_mess+"_"
    else:
        errors = True
        if silent_mode:
            status = "response not a list"
        else:
            print "P"+str(problem_id)+"reponse_must_be_list_"
            
    if errors == False:
        
        if silent_mode:
            status = "P"+str(problem_id)+"bin_pack_"
        else:
            print "Bins Packed for Problem ", str(problem_id)," ...." 
            print('Execution time: ' + str(myTime))
        
        if silent_mode:
            print status+"; num_ok: "+num_ok+"; num_over: "+num_over
        else:
            print "num_ok/num_over: ", num_ok,"/",num_over
        this_time = datetime.datetime.now()     # not use; formerly planned as iput to DB
        
