def refueling(d, m, n, stations):
    # Count of refills
    count = 0
    # Last refill
    last = 0
    # Tank volume
    volume = m

    if volume >= d:
        return 0

    while volume < d:
        if last >= n or stations[last] > volume:
            return -1
        while last < n - 1 and stations[last + 1] <= volume:
            last += 1

        count += 1
        volume = m + stations[last]
        last += 1

    return count


####
print(refueling(950, 400, 4, [200, 375, 550, 750]))  # 2
print(refueling(10, 3, 4, [1, 2, 5, 9]))  # -1
