<<<<<<< HEAD
# 플로이드 2
import sys
input = sys.stdin.readline
INF = 1e9

def tracer(i, j):
    if trace[i][j] == 0:
        return []
    
    k = trace[i][j]
    return tracer(i, k) + [k] + tracer(k, j)

N = int(input())
dp = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

trace = [[0] * (N+1) for _ in range(N+1)]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                trace[i][j] = k

for i in range(1, N+1):
    for j in range(1, N+1):
        print(dp[i][j] if dp[i][j] != INF else 0, end = ' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == 0 or dp[i][j] == INF:
            print(0)
            continue
        path = [i] + tracer(i, j) + [j]
        print(len(path), end=' ')
=======
# 플로이드 2
import sys
input = sys.stdin.readline
INF = 1e9

def tracer(i, j):
    if trace[i][j] == 0:
        return []
    
    k = trace[i][j]
    return tracer(i, k) + [k] + tracer(k, j)

N = int(input())
dp = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

trace = [[0] * (N+1) for _ in range(N+1)]

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                trace[i][j] = k

for i in range(1, N+1):
    for j in range(1, N+1):
        print(dp[i][j] if dp[i][j] != INF else 0, end = ' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == 0 or dp[i][j] == INF:
            print(0)
            continue
        path = [i] + tracer(i, j) + [j]
        print(len(path), end=' ')
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
        print(*path)