<<<<<<< HEAD
# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

weights = [0]
values = [0]

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

# 2차원 배열 사용
# dp = [[0] * (K+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         if j >= weights[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[N][K])

# 1차원 배열 사용
dp = [0] * (K+1)

for i in range(1, N+1):
    for j in range(K, 0, -1):
        if j >= weights[i]:
            dp[j] = max(dp[j], dp[j-weights[i]]+values[i])

=======
# 평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

weights = [0]
values = [0]

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

# 2차원 배열 사용
# dp = [[0] * (K+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         if j >= weights[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[N][K])

# 1차원 배열 사용
dp = [0] * (K+1)

for i in range(1, N+1):
    for j in range(K, 0, -1):
        if j >= weights[i]:
            dp[j] = max(dp[j], dp[j-weights[i]]+values[i])

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(dp[K])