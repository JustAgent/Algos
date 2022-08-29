with open("input.txt", "r") as input_file:
    s = input_file.readline()

n = len(s)
l = 0
prefix = [0 for i in range(1 + n)]

for i in range(1, n):
    while True:
        if s[l] == s[i]:
            l += 1
            break

        if l == 0:
            break

        l = prefix[l]
    
    prefix[i + 1] = l

period = n - prefix[n]

if n % period != 0:
    result = 1
else:
    result = n // period

with open("output.txt", "w") as output_file:
    output_file.write(str(result))
