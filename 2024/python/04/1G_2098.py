input = __import__('sys').stdin.readline
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
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N-1) for _ in range(N)] 

print(dfs(0,0))