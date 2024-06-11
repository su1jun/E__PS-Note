<<<<<<< HEAD
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    visited[cur] = 1
    for u in graph[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0], dp[u][1])

N = int(input())
cost = [0] + [int(x) for x in input().split()]

dp = [[0, cost[i]] for i in range(N+1)]
graph = collections.defaultdict(list)
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

dfs(1)
=======
import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur):
    visited[cur] = 1
    for u in graph[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0]
            dp[cur][0] += max(dp[u][0], dp[u][1])

N = int(input())
cost = [0] + [int(x) for x in input().split()]

dp = [[0, cost[i]] for i in range(N+1)]
graph = collections.defaultdict(list)
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

dfs(1)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(max(dp[1][1], dp[1][0]))