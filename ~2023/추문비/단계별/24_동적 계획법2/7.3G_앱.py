import sys
input = sys.stdin.readline
 
# 초기 입력
N, M = map(int, input().split()) # N: 활성화 된 어플, M: 필요 메모리
memory = [0] + list(map(int, input().split())) # 소요 메모리
cost = [0] + list(map(int, input().split())) # 필요 비용

dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(len(cost) + 1)]
result = sum(cost)
for i in range(1, len(cost)):
    for j in range(len(dp[1])):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - cost[i]] + memory[i], dp[i - 1][j])

        if dp[i][j] >= M:
            result = min(result, j)
if M != 0:
    print(result)
else:
    print(0)
