import sys
import heapq
input = sys.stdin.readline

def Dijkstra(n):
    weight[n] = 0
    heapq.heappush(heap, (0, n))

    while heap:
        wei, now =  heapq.heappop(heap)

        if weight[now] < wei:
            continue

        for w, next in graph[now]:
            next_wei = w + wei
            if next_wei < weight[next]:
                weight[next] = next_wei
                heapq.heappush(heap, (next_wei, next))

V = int(input())
E = int(input())

INF = sys.maxsize
weight = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
start, end = map(int, input().split())

Dijkstra(start)
print(weight[end])