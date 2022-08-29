def max_gold(volume, base_ingots):
    ingots = [0] + base_ingots
    dict_ingots = {}

    for i in range(0, volume + 1):
        dict_ingots[(i, 0)] = 0
    for i in range(len(ingots)):
        dict_ingots[(0, i)] = 0
    print(dict_ingots)
    for i in range(1, len(ingots)):
        for weight in range(1, volume + 1):
            dict_ingots[(weight, i)] = dict_ingots[(weight, i - 1)]

            if ingots[i] <= weight:
                val = dict_ingots[(weight - ingots[i], i - 1)] + ingots[i]

                if dict_ingots[(weight, i)] < val:
                    dict_ingots[(weight, i)] = val
    print(dict_ingots)
    return max(dict_ingots.values())


result = max_gold(10, [1, 4, 8])
print(result)
