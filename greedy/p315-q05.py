from sys import stdin
from itertools import combinations
N,M = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

balls = [0] * (M+1)
nums = set()
for num in arr:
  nums.add(num)
  balls[num] += 1

comb = list(combinations(nums,2))
ans = 0
for c in comb:
  b1,b2 = c
  ans += (balls[b1] * balls[b2])

print(ans)
