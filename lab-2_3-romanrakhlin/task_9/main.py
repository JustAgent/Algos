def main():
    with open("input.txt") as input_file:
        V, E = map(int, input_file.readline().split())
        graph = [list(map(int, line.split())) for line in input_file]

    def is_negative_cycle_bellman_ford(src, dist):
        for i in range(V):
            dist[i] = 10**18

        dist[src] = 0
      
        for i in range(1, V):
            for j in range(E):
                u = graph[j][0]
                v = graph[j][1]
                weight = graph[j][2]
                if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
                    dist[v] = dist[u] + weight
      
        for i in range(E):
            u = graph[i][0]
            v = graph[i][1]
            weight = graph[i][2]
            if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
                return True
      
        return False

    visited = [0] * V
    dist = [0] * V
    result = 0 # RESULT!!!!
  
    for i in range(V):
        if (visited[i] == 0):
            if is_negative_cycle_bellman_ford(i, dist):
                result = 1
                return
  
            for i in range(V):
                if (dist[i] != 10 ** 18):
                    visited[i] = True
       
    with open("output.txt", "w") as output_file:
        output_file.write(str(result))

if __name__ == "__main__":
    main()

