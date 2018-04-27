# -*- coding: utf-8 -*-
def load_knapsack(things,knapsack_cap):
    my_team_number_or_name="jdeng01"
    
    def bestvalue(i, j):
        if i == 0: return 0
        weight, value = things.values()[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)
            
    #this section creates the result list using the best results from the preceding section
    j = knapsack_cap
    items_to_pack = []
    for i in xrange(len(things), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            items_to_pack.append(things.items()[i-1][0])
            j -= things.values()[i - 1][0]
            
    items_to_pack.reverse()  
    return my_team_number_or_name,items_to_pack
