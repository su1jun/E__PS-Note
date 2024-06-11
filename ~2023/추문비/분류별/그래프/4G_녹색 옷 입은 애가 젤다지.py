import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra():
    step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]

    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))

    while heap:
        wei, px, py = heapq.heappop(heap)

        if distance[px][py] < wei:
            continue

        for x, y in step:
            nx = px + x
            ny = py + y
            if 0 <= nx < N and 0 <= ny < N:
                next_wei = graph[nx][ny] + wei
                if next_wei < distance[nx][ny]:
                    distance[nx][ny] = next_wei
                    heapq.heappush(heap, (next_wei, nx, ny))

    return distance[-1][-1]

p = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(f"Problem {p}: {dijkstra()}")
    p += 1