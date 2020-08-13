from sys import stdin


def find_parent(parent,n):
  if parent[n] != n:
    return find_parent(parent,parent[n])
  else:
    return n

def check_team(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a==b:
    print("YES")
  else:
    print("NO")


def union_team(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

  return

n,m = map(int,stdin.readline().split())
parent = [[] for i in range(n+1)]
for i in range(1,n+1):
  parent[i] = i


for i in range(m):
  command,a,b = map(int,stdin.readline().split())
  if command==0:
    union_team(parent,a,b)
  else:
    check_team(parent,a,b)
