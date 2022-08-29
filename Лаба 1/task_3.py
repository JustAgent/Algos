def max_income(n, a, b):
    result = 0
    a.sort()
    b.sort()

    for i in range(n):
        result += a[i] * b[i]

    return result


#####
print(max_income(1, [23], [39]))
print(max_income(3, [1, 3, -5], [-2, 4, 1]))
