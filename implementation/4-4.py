from sys import stdin

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = list(map(int, stdin.readline().split()))
x, y, now_dir = list(map(int, stdin.readline().split()))
place = [[0] * m for _ in range(n)]

for i in range(n):
    place[i] = list(map(int, stdin.readline().split()))

flag_stop = False
flag_found = False

cnt = 1
while not flag_stop:
    for i in range(4, 0, -1):
        flag_found = False
        row = x + move[(now_dir + i) % 4][0]
        col = y + move[(now_dir + i) % 4][1]
        if 0 <= row < n and 0 <= col < m and place[row][col] == 0:
            x, y = row, col
            now_dir = (now_dir + i) % 4
            place[row][col] = 1
            cnt += 1
            flag_found = True
            break
    if not flag_found:
        flag_stop = True

print(cnt)
