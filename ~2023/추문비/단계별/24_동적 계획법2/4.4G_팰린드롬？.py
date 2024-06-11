import sys
input = sys.stdin.readline
 
# 초기 입력
N = int(input())
nums = [list(map(int, input().split()))] * N
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if nums[i+1][i] == nums[i][i+1]:
        dp[i][i+1] = 1

for i in range(2, N): # col
    for j in range(i-1, -1, -1): # row
        if nums[j][i] == nums[i][j] and dp[j+1][i-1]:
            dp[j][i] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
