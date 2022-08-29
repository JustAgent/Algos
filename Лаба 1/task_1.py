def max_worth(volume, array):
    worth = {}
    weight = {}
    for i in range(len(array)):
        worth[i] = array[i][0] / array[i][1]
        weight[i] = array[i][1]
    worth = dict(sorted(worth.items(), reverse=True, key=lambda x: x[1]))
    list_order = list(worth.keys())
    capacity = 0
    i = 0
    result = 0
    while capacity != volume:
        if capacity + weight[list_order[i]] <= volume:
            capacity += weight[list_order[i]]
            result += weight[list_order[i]] * worth[list_order[i]]
            i += 1
        else:
            m = volume - capacity
            capacity += m
            result += m * worth[list_order[i]]
    print(result)


###TESTS
n1 = 50
n2 = 10
n3 = 70
test1 = [[60, 20], [100, 50], [120, 30]]
test2 = [[500, 30]]
test3 = [[500, 30], [600, 30], [400, 25], [10, 1]]
max_worth(n1, test1)
max_worth(n2, test2)
max_worth(n3, test3)
