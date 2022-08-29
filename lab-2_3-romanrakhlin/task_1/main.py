def main():
    with open("input.txt", "r") as input_file:
        n, m = map(int, input_file.readline().split())
        graph = []

        for _ in range(n):
            graph.append([])

        for _ in range(m):
            u, v = map(int, input_file.readline().split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        visited = [0] * n
        start, final = map(int, input_file.readline().split())
        start -= 1
        final -= 1

    def dfs(node):
        visited[node] = 1
        if node == final:
            return
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)

    dfs(start)

    with open("output.txt", "w") as output_file:
        if visited[final]:
            output_file.write("1")
        else:
            output_file.write("0")

if __name__ == "__main__":
    main()

