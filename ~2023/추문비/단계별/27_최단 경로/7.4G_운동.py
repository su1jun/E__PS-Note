import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    while heap:
        wei, now, goal = heapq.heappop(heap)

        if now == goal:
            return wei

        if distance[now][goal] < wei:
            continue

        for w, next in graph[goal]:
            next_wei = w + wei
            if distance[now][next] > next_wei:
                distance[now][next] = next_wei
                heapq.heappush(heap, [next_wei, now, next])
    return -1


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
distance = [[INF] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    distance[a][b] = c
    heapq.heappush(heap, [c, a, b])

print(dijkstra())