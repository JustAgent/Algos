def splitter(array, n):
    left_sum = 0
    for i in range(0, n):
        left_sum += array[i]
    right_sum = 0
    for i in range(n - 1, -1, -1):
        right_sum += array[i]
        left_sum -= array[i]
        if right_sum == left_sum:
            return i
        if right_sum > left_sum:
            return -1


def printer(arr, n):
    split_point = splitter(arr, n)
    if split_point == -1 or split_point == n:
        print(-1)
        return

    for i in range(0, n):
        if split_point == i:
            print("")
        print(arr[i], end=" ")

    print()


# Тетсты
arr = [1, 2, 3, 3, 3, 2, 2, 1, 1, 6]
arr2 = [1, 2, 3]
printer(arr, len(arr))
printer(arr2, len(arr2))
