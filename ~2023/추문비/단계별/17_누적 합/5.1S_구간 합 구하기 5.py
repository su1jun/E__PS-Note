import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0 for _ in range(N+1)]]

data = list(map(int, input().split()))
for j in range(1, N):
    data[j] += data[j-1]
dp.append([0] + data)

if N > 1:
    for i in range(1, N):
        data = list(map(int, input().split()))
        for j in range(1, N):
            data[j] += data[j-1]
            data[j-1] += dp[i][j]
        data[-1] += dp[i][-1]
        dp.append([0] + data)
print(f"dp : {dp}")

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

    
