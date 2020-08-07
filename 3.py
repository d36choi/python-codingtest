from sys import stdin

N, M = list(map(int, stdin.readline().split()))

arr = [ [0] * M for _ in range(N)]
min_arr = [ 0 for _ in range(N)]
for i in range(N):
    row = list(map(int, stdin.readline().split()))
    for j in range(M):
        arr[i][j] = row[j]

    min_arr[i] = min(arr[i])

print(max(min_arr))
