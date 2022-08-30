def main():
    inf = float("inf")
    with open("input.txt") as input_file:
        n, m = map(int, input_file.readline().split())
        d = [inf for _ in range(n * n + 2)]
        for i in range(m):
            u, v = map(int, input_file.readline().split())
            
            u -= 1
            v -= 1
            
            d[u * n + v] = 0
            
            if d[v * n + u] == inf:
                d[v * n + u] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i * n + k] != inf and d[k * n + j] != inf:
                        d[i * n + j] = min(d[i * n + j], d[i * n + k] + d[k * n + j])
        
        result = 0

        for i in range(n):
            for j in range(n):
                if d[i * n + j] != inf:
                    result = max(result, d[i * n + j])

    with open('output.txt', 'w') as output_file:
        output_file.write(str(result))

if __name__ == "__main__":
    main()

