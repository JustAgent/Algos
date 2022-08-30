def main():
    with open("input.txt") as input_file:
        n, m = map(int, input_file.readline().split())
        
        matrix = [[] for _ in range(n)]

        for i in range(n):
            row = input_file.readline()
            for j in range(m):
                matrix[i].append(row[j])

    def dfs(matrix, m, n):
        result = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "#":
                    result += 1
                    matrix = _dfs(i, j, matrix, m, n)

        return result

    def _dfs(i, j, matrix, m, n):
        stack = [(i, j)]
            
        while len(stack) > 0:
            matrix[i][j] = "."

            if j + 1 < m:
                if matrix[i][j + 1] == "#":
                    stack.append((i, j + 1))
            if j - 1 >= 0:
                if matrix[i][j - 1] == '#':
                    stack.append((i, j - 1))
            if i + 1 < n:
                if matrix[i + 1][j] == '#':
                    stack.append((i + 1, j))
            if i - 1 >= 0:
                if matrix[i - 1][j] == "#":
                    stack.append((i - 1, j))

            (i, j) = stack.pop()

        return matrix

    with open("output.txt", "w") as output_file:
        output_file.write(str(dfs(matrix, m, n)))

if __name__ == "__main__":
    main()
