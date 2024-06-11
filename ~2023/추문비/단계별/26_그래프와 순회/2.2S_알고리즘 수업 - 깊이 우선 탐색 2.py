import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M, R = map(int, input().split()) # N : 정점 갯수, M : 간선 갯수, R = 시작 정점
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1) # 방문처리
ans = ["0"] * (N+1) # 방문순서
order = 1 # 순서계산
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n): # n : 방문 정점, m : 방문 순서
    global order
    visited[n] = 1
    ans[n] = str(order)
    order += 1
    for i in sorted(graph[n], reverse=True):
        if not visited[i]:
            dfs(i)
    
dfs(R)
print("\n".join(ans[1:]))

