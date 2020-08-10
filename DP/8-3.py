from sys import stdin


n,m = map(int,stdin.readline().split())
array = [10001] * (10001)
check = [10001] * (10001)
for i in range(n):
  index = int(input())
  array[index] = 1
  check[index] = 1


for i in range(1,m+1):
  for j in range(1,i):
    if check[i] == 1:
      break
    if array[i-j] != 10001:
      array[i] = min(array[i],array[i-j]+array[j])
      

if array[m] == 10001:
  print("-1")
else:
  print(array[m])


    
  
