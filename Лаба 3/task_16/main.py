from collections import deque

def main():
    def is_recursive(graph, procedure):
        queue = deque()
        visited = set()
        inqueue = set()
        queue.append(procedure)
        inqueue.add(procedure)
        while len(queue) > 0:
            c = queue.popleft()
            inqueue.remove(c)
            visited.add(c)
            for v in graph[c]:
                if v == procedure:
                    return True
                if v not in visited and v not in inqueue:
                    queue.append(v)
                    inqueue.add(v)
        return False
        
    with open("input.txt") as input_file:
        n = int(input_file.readline())

        graph = {}
        res = []
        pcs = []

        for _ in range(n):
            procedure = input_file.readline().strip()
            pcs.append(procedure)
            n = int(input_file.readline())
            calls = [input_file.readline().strip() for _ in range(n)]
            graph[procedure] = calls
            input_file.readline()

        for procedure in pcs:
            res.append("YES" if is_recursive(graph, procedure) else "NO")
    
    with open("output.txt", "w") as output:
        output.write("\n".join(res))

if __name__ == "__main__":
    main()

