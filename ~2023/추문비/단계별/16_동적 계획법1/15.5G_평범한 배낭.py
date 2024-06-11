import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
# print(f"data : {data}")

for i in range(1, N+1):
    w = data[i-1][0]
    v = data[i-1][1]
    for j in range(1, K+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# print(dp)
print(f"{dp[-1][-1]}")


