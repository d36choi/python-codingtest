from sys import stdin, stdout

N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort()
B.sort(reverse=True)
count = 0
for i in range(N):
    if A[i] < B[i] and count < K:
        A[i] = B[i]
        count += 1
    else:
        break

print(sum(A))
