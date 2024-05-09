import math, sys
input = sys.stdin.readline
INF = (1e9)

def dfs(i, visited):
    if dp[i][visited] != 0: return dp[i][visited]

    if visited == (1 << (N-1)) - 1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return INF

    min_visited = INF

    for j in range(1, N):
        if not graph[i][j]: continue
        if visited & (1 << j-1): continue

        D = graph[i][j] + dfs(j, visited | (1 << (j-1)))
        if min_visited > D: min_visited = D

    dp[i][visited] = min_visited

    return min_visited

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * N for _ in range(N)]

for i in range(N-1):
    x1, y1 = cost[i]
    for j in range(i+1, N):
        x2, y2 = cost[j]
        graph[i][j] = graph[j][i] = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

dp = [[0] * (1 << N-1) for _ in range(N)] 

print(dfs(0,0))