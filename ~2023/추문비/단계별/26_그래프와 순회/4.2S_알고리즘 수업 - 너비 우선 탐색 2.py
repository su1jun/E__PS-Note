import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M, R = map(int, input().split()) # N : 정점 갯수, M : 간선 갯수, R = 시작 정점
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1) # 방문처리
Q = deque() # 방문큐
ans = [] # 답
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n): # n : 방문 정점, m : 방문 순서
    global cnt
    visited[n] = 1
    ans.append(n)
    for i in sorted(graph[n]):
        if not visited[i]:
            dfs(i)

def bfs(n): # n : 방문 정점, m : 방문 순서
    Q.append(n)
    visited[n] = 1
    while Q:
        n = Q.popleft()
        ans.append(n)
        for i in sorted(graph[n]):
            if not visited[i]:
                visited[i] = 1
                Q.append(i)

dfs(R)
print(*ans)
ans = [] # 답

visited = [0] * (N+1) # 방문처리
bfs(R)
print(*ans)