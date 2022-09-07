import sys

M1 = 10 ** 9 + 7
M2 = 998244353
x = 29


def get_hashes(ss, M):
    n = len(ss)
    hash = [0] * (n + 1)
    for i in range(n):
        hash[i + 1] = (hash[i] * x % M + ord(ss[i]) - ord('a')) % M
    return hash


def get_pows(n, M):
    pw = [1] * (n + 1)
    for i in range(1, n + 1):
        pw[i] = pw[i - 1] * x % M
    return pw


def check(k):
    if k == 0:
        return (0, 0)
    idx = dict()
    for i in range(n + 1 - k):
        h1 = (s1[i + k] - s1[i] * pow1[k]) % M1
        h2 = (s2[i + k] - s2[i] * pow2[k]) % M2
        idx[(h1, h2)] = i
    for i in range(m + 1 - k):
        h1 = (t1[i + k] - t1[i] * pow1[k]) % M1
        h2 = (t2[i + k] - t2[i] * pow2[k]) % M2
        if (h1, h2) in idx:
            return idx[(h1, h2)], i
    return -1, -1


sys.stdin = open('input.txt', "r")
with open('output.txt', 'w') as f_out:
    for line in sys.stdin:
        s, t = line.split()
        n, m = len(s), len(t)
        s1 = get_hashes(s, M1)
        s2 = get_hashes(s, M2)
        t1 = get_hashes(t, M1)
        t2 = get_hashes(t, M2)
        pow1 = get_pows(max(n, m), M1)
        pow2 = get_pows(max(n, m), M2)
        l, r = 0, n + 1
        while r - l > 1:
            mid = (r + l) // 2
            i1, i2 = check(mid)
            if i1 == -1:
                r = mid
            else:
                l = mid

        res = " ".join(map(str, check(l))) + " " + str(l)

        f_out.write(res + "\n")
