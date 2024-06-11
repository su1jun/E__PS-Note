import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if visited[a] == -1:
            visited[a] = wei + b
            dfs(a, wei + b)

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (N+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (N+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))