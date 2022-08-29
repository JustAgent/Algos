def lectures(array):
    sorted_array = sorted(array, key=lambda x: x[1])
    #print(sorted_array)
    end_hour = 0
    count = 1
    for i in range(1, len(sorted_array)):
        if sorted_array[i][0] >= sorted_array[end_hour][1]:
            count += 1
            end_hour = i
    return count


test = [[5, 6], [1, 5], [2, 3], [5, 8], [12, 20], [3, 4], [1, 2]]

print(lectures(test))
