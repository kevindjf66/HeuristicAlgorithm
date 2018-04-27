# Transportation Operation Optimization

def trans(dist, dcs, stores_vol):
    my_team_or_name = "jdeng01"
    result = []
    visited = []
    new_dcs = {key: list(dcs[key]) for key in dcs}
    new_dist = dist.items()
    sort_dist = sorted(new_dist, key=lambda x: x[1])
    new_stores = {i[0]:i[1] for i in stores_vol}
    while len(result) < len(stores_vol):
        for ds, distance in sort_dist:
            if ds[1] in visited:
                continue
            else:
                temp_cap = new_dcs[ds[0]][0] - new_stores[ds[1]]
                temp_doors = new_dcs[ds[0]][1] - 1
                temp_drivers = new_dcs[ds[0]][2] - new_stores[ds[1]]/4000
                if temp_cap < 0 or temp_doors < 0 or temp_drivers < 0:
                    continue
                else:
                    new_dcs[ds[0]][0] = temp_cap
                    new_dcs[ds[0]][1] = temp_doors
                    new_dcs[ds[0]][2] = temp_drivers
                    ds = (ds[1], ds[0])
                    visited.append(ds[0])
                    result.append(ds)
                    break
    return my_team_or_name, result
