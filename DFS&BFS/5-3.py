from sys import stdin

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, stdin.readline().split())
ices = [[0] * m for i in range(n)]
res = 0


def DFS(i, j):
    global ices
    ices[i][j] = 1
    for index in range(4):
        row = i + move[index][0]
        col = j + move[index][1]
        if 0 <= row < n and 0 <= col < m and ices[row][col] == 0:
            DFS(row, col)
    return

for i in range(n):
    row = stdin.readline()
    for j in range(m):
        ices[i][j] = int(row[j])

for i in range(n):
    for j in range(m):
        if ices[i][j] == 0:
            DFS(i, j)
            res += 1

print(res)
