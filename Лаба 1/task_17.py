def f(n):
    array = [[0 for j in range(n + 1)] for i in range(10)]
    mod = 10 ** 9
    for i in range(10):
        array[i][1] = 1

    for num in range(2, n + 1):
        for k in range(10):
            match k:
                case 0:
                    array[0][num] = (array[4][num - 1] + array[6][num - 1]) % mod
                case 1:
                    array[1][num] = (array[6][num - 1] + array[8][num - 1]) % mod
                case 2:
                    array[2][num] = (array[9][num - 1] + array[7][num - 1]) % mod
                case 3:
                    array[3][num] = (array[8][num - 1] + array[4][num - 1]) % mod
                case 4:
                    array[4][num] = (array[0][num - 1] + array[3][num - 1] + array[9][num - 1]) % mod
                case 6:
                    array[6][num] = (array[0][num - 1] + array[1][num - 1] + array[7][num - 1]) % mod
                case 7:
                    array[7][num] = (array[6][num - 1] + array[2][num - 1]) % mod
                case 8:
                    array[8][num] = (array[1][num - 1] + array[3][num - 1]) % mod
                case 9:
                    array[9][num] = (array[2][num - 1] + array[4][num - 1]) % mod
    #print(array)
    total_sum = 0
    for i in range(1, 10):
        if i != 8:
            #print("array: ", array[i][n])
            total_sum = (total_sum + array[i][n]) % mod

    return total_sum


print(f(1))
print(f(2))
print(f(1000000))


