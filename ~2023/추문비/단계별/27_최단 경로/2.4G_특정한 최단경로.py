import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    distance = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

v1, v2 = map(int, input().split())

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[V]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[V]

result = min(v1_path, v2_path)
print(result if result < INF else -1)