from collections import defaultdict

def main():
    with open("input.txt") as input_file:
        n = int(input_file.readline())
        d, v = map(int, input_file.readline().split())
        r = int(input_file.readline())
        graph = defaultdict(list)
        
        for line in f:
            dep, start_time, dest, end_time = map(int, line.split())
            graph[dep].append((start_time, dest, end_time))

        time = [float("inf") for _ in range(N + 1)]
        time[d] = 0
        visited = set()
        
        while True:
            min_time = float("inf")
            
            for i in range(1, N + 1):
                if i not in visited and time[i] < min_time:
                    min_time = time[i]
                    min_village = i

            if min_time == float("inf"):
                break

            start = min_village
            visited.add(start)

            for start_time, finish, finish_time in graph[start]:
                if time[start] <= start_time and finish_time < time[finish]:
                    time[finish] = finish_time

    with open("output.txt", "w") as output:
        output.write(str(-1 if time[v] == float("inf") else time[v]))

if __name__ == "__main__":
    main()