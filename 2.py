from sys import stdin

N, M, K = list(map(int, stdin.readline().split()))

arr = list(map(int , stdin.readline().split()))

arr.sort(reverse=True)

res = 0
for i in range(1,M+1):
    if i%K == 0:
        res += arr[1]
    else:
        res += arr[0]

print(res)



