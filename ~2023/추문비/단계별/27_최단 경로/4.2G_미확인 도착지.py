import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if distance[now] < wei:
            continue

        for w, next in graph[now]:
            next_wei = w + distance[now]
            if next_wei < distance[next]:
                distance[next] = next_wei
                heapq.heappush(heap, (next_wei, next))
    return distance

for _ in range(int(input())):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        if (a == G and b == H) or (a == H and b == G):
            d -= 0.1
        graph[a].append([d, b])
        graph[b].append([d, a])
    distance = dijkstra(S)

    targets = [int(input()) for _ in range(T)]
    targets.sort()
    for target in targets:
        if distance[target] != INF and type(distance[target]) == float:
            print(target, end=' ')

    print()

    
