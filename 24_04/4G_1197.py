import sys
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
visited = [0] * (V+1)
graph = [[0] * V+1 for _ in range(V+1)]

for _ in range(V):
    a, b, c = map(int, input().split())
    graph[a][b] = c