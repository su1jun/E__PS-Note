<<<<<<< HEAD
from collections import defaultdict
import heapq
input = __import__('sys').stdin.readline
INF = int(1e9)

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    dist[start] = 0
    while que:
        wei, node = heapq.heappop(que)
        if dist[node] < wei:
            continue

        for nt_node, nt_wei in graph[node]:
            cost = wei + nt_wei

            if cost < dist[nt_node]:
                dist[nt_node] = cost
                heapq.heappush(que, (cost, nt_node))
                pre_node[nt_node] = node
    return
    
N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF] * (N+1)
pre_node = [0] * (N+1)

dijkstra(start)
print(dist[end])

path = [end]
now = end
while now != start:
    now = pre_node[now]
    path.append(now)

print(len(path))
=======
from collections import defaultdict
import heapq
input = __import__('sys').stdin.readline
INF = int(1e9)

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    dist[start] = 0
    while que:
        wei, node = heapq.heappop(que)
        if dist[node] < wei:
            continue

        for nt_node, nt_wei in graph[node]:
            cost = wei + nt_wei

            if cost < dist[nt_node]:
                dist[nt_node] = cost
                heapq.heappush(que, (cost, nt_node))
                pre_node[nt_node] = node
    return
    
N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF] * (N+1)
pre_node = [0] * (N+1)

dijkstra(start)
print(dist[end])

path = [end]
now = end
while now != start:
    now = pre_node[now]
    path.append(now)

print(len(path))
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(*path[::-1])