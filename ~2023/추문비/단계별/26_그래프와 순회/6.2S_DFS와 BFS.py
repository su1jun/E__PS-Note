import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split()) # N : 정점 갯수, M : 간선 갯수, V = 시작 정점
graph = [[] for _ in range(N+1)]
visited = ["0"] * (N+1) # 방문처리
Q = deque() # 방문큐

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(n): # n : 방문 정점, m : 방문 순서
    cnt = 1 # 방문순서
    Q.append(n)
    visited[n] = "1"
    while Q:
        for i in sorted(graph[Q.popleft()], reverse=True):
            if visited[i] == "0":
                cnt += 1
                visited[i] = str(cnt)
                Q.append(i)

bfs(V)

print("\n".join(visited[1:]))