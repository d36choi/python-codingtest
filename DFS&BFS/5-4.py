from sys import stdin
from _collections import deque


def BFS(n,m):
    global queue
    queue.append((0,0,1))
    while queue:
        row, col, cnt = deque.popleft(queue)
        # queue.popleft()
        if row == n-1 and col == m-1:
            print(cnt)
            return

        if 0 <= row + 1 < n and maze[row + 1][col] == 1:
            deque.append(queue, (row + 1, col, cnt + 1))
        if 0 <= col + 1 < m and maze[row][col + 1] == 1:
            deque.append(queue, (row, col + 1, cnt + 1))


move = [[1, 0], [0, 1]]

n, m = map(int, stdin.readline().split())
maze = [[0] * m for i in range(n)]
res = 0
queue = deque()

for i in range(n):
    row = stdin.readline()
    for j in range(m):
        maze[i][j] = int(row[j])
BFS(n,m)
