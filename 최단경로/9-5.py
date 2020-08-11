from sys import stdin
import heapq

def dijkstra(c):
  distance = [INF] * (n+1)
  visited = [0] * (n+1)
  queue = []
  heapq.heappush(queue,(0,c))
  distance[c] = 0
  while queue:
    length,node = heapq.heappop(queue)
    for y,z in graph[node]:
      if visited[y] == 0:
        heapq.heappush(queue,(z,y))
      if distance[y] > length+z:
        distance[y] = length+z
    visited[node] = 1
    cnt = -1
  for i in range(n+1):
    if distance[i] == INF:
      distance[i] = 0
    else:
      cnt += 1
  print(cnt,max(distance))

# main
INF = int(1e9)
n,m,c = map(int,stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
  x,y,z = map(int,stdin.readline().split())
  graph[x].append((y,z))




dijkstra(c)

 

