# Minimum Spanning Tree

dist = {(7L, 3L): 2.4498384789254177, (6L, 9L): 6.558122303116606,
        (18L, 4L): 7.372616595153464, (15L, 1L): 7.827072930017223,
        (1L, 11L): 7.858190677784387, (4L, 0L): 3.7369050221959563,
        (9L, 0L): 5.090028540310345, (6L, 7L): 1.2234426713365525,
        (9L, 21L): 3.4213787728910634, (15L, 11L): 8.864256498692638,
        (18L, 9L): 9.272772628700368, (15L, 4L): 5.102697814208576,
        (9L, 3L): 7.65995883448742, (6L, 0L): 3.3985668833755858,
        (15L, 29L): 12.605191095654083, (2L, 11L): 4.477428971345286,
        (4L, 21L): 5.320467096219641, (18L, 0L): 7.1726447761202765,
        (7L, 21L): 10.97954032665383, (3L, 11L): 2.4547202353225153,
        (2L, 1L): 4.722402761154496, (15L, 105L): 4.9064423653964875,
        (0L, 105L): 3.611245089377697, (7L, 2L): 1.6466919630347743,
        (6L, 29L): 9.08141917394657, (29L, 105L): 8.433269129416258,
        (15L, 0L): 6.850951531439121, (0L, 11L): 5.124361270193993,
        (4L, 1L): 3.0220762632187395, (4L, 105L): 5.2224243588557995,
        (2L, 105L): 1.359763433189901, (7L, 1L): 6.2779921417815885,
        (6L, 11L): 4.570700226961059, (18L, 6L): 3.7799515009072695,
        (15L, 7L): 5.4857272007273, (21L, 11L): 13.444573740527028,
        (1L, 0L): 2.789642671456705, (4L, 11L): 8.377900785978051,
        (4L, 6L): 4.619643112527783, (6L, 1L): 5.68682948348248,
        (21L, 105L): 10.542196114893997, (3L, 105L): 2.851071873835663,
        (1L, 105L): 6.081622884395292, (15L, 9L): 6.6505088000039825,
        (18L, 11L): 6.691323419810101, (2L, 29L): 9.38009054697701,
        (1L, 3L): 5.41460394481151, (9L, 29L): 15.23707746840322,
        (6L, 2L): 1.0502664530561194, (7L, 11L): 3.3978626048465226,
        (18L, 21L): 12.34896743744257, (18L, 1L): 9.241999753554849,
        (6L, 105L): 0.6481739318647229, (21L, 1L): 6.009292105679634,
        (9L, 11L): 10.061863663089618, (18L, 2L): 4.8277722058286345,
        (15L, 3L): 7.559837846830138, (9L, 105L): 7.146662423912176,
        (2L, 3L): 2.57267307867217, (4L, 2L): 4.077395887593821,
        (4L, 29L): 13.445205211536555, (7L, 0L): 3.666162861970769,
        (15L, 21L): 9.228582177679936, (21L, 29L): 18.649724313635108,
        (11L, 29L): 5.3072910601212655, (18L, 7L): 4.0120043759587025,
        (15L, 6L): 4.431018718530056, (7L, 105L): 0.6016317423003813,
        (4L, 7L): 5.67184746192079, (9L, 1L): 3.189023863770686,
        (6L, 21L): 9.939303247159161, (1L, 29L): 13.165074269036989,
        (0L, 3L): 2.6698106832479938, (7L, 29L): 7.883340790621384,
        (4L, 9L): 1.9587782950532175, (2L, 9L): 5.941289142037911,
        (11L, 105L): 3.99566803704013, (6L, 3L): 3.1603516641088403,
        (15L, 18L): 3.7615906491085496, (0L, 29L): 10.417674076118637,
        (21L, 0L): 8.388035561221376, (18L, 105L): 3.7290647679029507,
        (7L, 9L): 7.567937102685498, (18L, 3L): 6.456366045443866,
        (15L, 2L): 5.063134770115016, (2L, 21L): 9.35963011841758,
        (21L, 3L): 11.017883811636137, (2L, 0L): 2.3483118178339812,
        (18L, 29L): 9.277979753712971, (4L, 3L): 6.06638725248541,
        (3L, 29L): 7.754426940710928}

locs = [[15L, 36.72361, -76.30627, '504 Bud Drive, Chesapeake, Chesapeake, VA  23322-7460', 'store'],
        [18L, 36.7162164893, -76.238979609, '237 S Battlefield Blvd Unit 13, Great Bridge Shopping Center, Chesapeake, VA  23322-5231', 'store'],
        [4L, 36.7953056906, -76.3283841439, '2044 Victory Blvd, Williams Court I, Portsmouth, VA  23702-2642', 'store'],
        [6L, 36.7700576963, -76.2510840346, '1509 Sams Circle., Sams Shopping Center, Chesapeake, VA  23320-4694', 'store'],
        [7L, 36.7737810811, -76.2294727027, '1320 Greenbrier Pkwy Suite 320, Greenbrier Market Center, Chesapeake, VA  23320-0746', 'store'],
        [2L, 36.784765, -76.25588, '1973 S. Military Hwy., Chesapeake Crossing, Chesapeake, VA  23320-4422', 'store'],
        [9L, 36.8103296, -76.3584096, '4036 Victory Blvd, Victory Crossing, Portsmouth, VA  23701-2820', 'store'],
        [21L, 36.82249, -76.41837, '4300 Portsmouth Blvd Suite 170, Chesapeake Center, Chesapeake, VA  23321-2137', 'store'],
        [1L, 36.8368239286, -76.3111960714, '1112 London Blvd, London Plaza, Portsmouth, VA  23704-2246', 'store'],
        [0L, 36.8176, -76.26684, '1800 Liberty Street Ste 106, Liberty Plaza, Chesapeake, VA  23324-3569', 'store'],
        [3L, 36.80841, -76.21996, '1105 South Military Hwy, Castle Shops, Chesapeake, VA  23320-2343', 'store'],
        [11L, 36.7993833134, -76.1770448516, '1385 Fordham Dr. #113, KempsRiver Crossing, Virginia Beach, VA  23464-5345', 'store'],
        [29L, 36.772852, -76.087036, '3332 Princess Anne Rd, Landstown Commons, Virginia Beach, VA  23456-2613', 'store'],
        [105L, 36.770187, -76.239374, '1330 Executive Blvd, Chesapeake, Virginia 23320', 'dc']]
'''
def mst_algo(locs, dist):
    name_or_team = "jdeng01"
    mst = []
    ids = [h[0] for h in locs]
    dist1 = dist
    for i in ids:
        if len(mst) == len(ids) - 1:
            break
        else:
            possible_cons = [key for key in dist1.keys() if i in key]
            dist2 = {x: dist1[x] for x in possible_cons}
            con = min(dist2, key=dist2.get)
            mst.append(con)
            dist1 = {key: value for key, value in dist1.items()
             if key is not con}
    return name_or_team, mst

def mst_algo(locs, dist):
    name_or_team = "jdeng01"
    mst = []
    ids = [h[0] for h in locs]
    start = ids[0]
    ids.remove(start)
    connected = []
    connected.append(start)
    while len(mst) < len(locs):
        temp = dist[max(dist, key = dist.get)]
        for c in connected:
            for i in ids:
                if dist[(c, i)] < temp:
                    new_con = (c, i)
                    temp = dist[(c, i)]
        connected.append(new_con[1])
        ids.remove(new_con[1])
        mst.append(new_con)
    return name_or_team, mst
'''

name_or_team = "jdeng01"
mst = [(None, None)]
nodes = sorted([h[0] for h in locs])
visited = []
dist1 = dist
while len(mst) < len(locs):
    distan = float('inf')
    for s in nodes:
        for d in nodes:
            if s in visited and d in visited or s == d:
                continue
            try:
                temp_dist = dist1[(s, d)]
                if temp_dist < distan:
                    distan = dist1[(s, d)]
                    pre = s
                    n = d
            except:
                continue
    con = (pre, n)
    if con == mst[-1]:
        unconnect = [h for h in visited if visited.count(h) == 1]
        distan2 = float('inf')
        for i in unconnect:
            for j in unconnect:
                if i == j:
                    continue
                try:
                    temp = dist1[(i, j)]
                    if temp < distan2:
                        distan2 = temp
                        c1 = i
                        c2 = j
                except:
                    continue
        con = (c1, c2)
        mst.append(con)
    else:
        mst.append(con)
        visited.append(pre)
        visited.append(n)

        
def distance(mst, dist):
    distan = 0
    for key in mst:
        distan = distan + dist[key]
    return distan
