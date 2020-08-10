from sys import stdin

array = [30001] * 30000

def dp(n,count):
  if n==1:
    if array[n] > count:
      array[n] = count  
    return
  else:
    if array[n] != 0 and array[n] < count:
      return
    else:
      array[n] = count
      if n%5==0:
        dp(n//5,count+1)
      if n%3==0:
        dp(n//3,count+1)
      if n%2==0:
        dp(n//2,count+1)
      if n>1:
        dp(n-1,count+1)
  

n = int(stdin.readline())
dp(n,0)
print(array[1])
