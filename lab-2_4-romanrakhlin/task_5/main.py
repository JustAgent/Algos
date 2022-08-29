def prefix_function(s):
    n = len(s)
    pi = [0 for i in range(n)]
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

with open("input.txt", "r") as input_file:
    result = prefix_function(input_file.readline())

with open("output.txt", "w") as output_file:
    output = ""
    for x in result:
        output += str(x) + " "
    output_file.write(output[:len(output) - 1])