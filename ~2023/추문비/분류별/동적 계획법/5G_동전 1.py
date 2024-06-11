import sys
input = sys.stdin.readline
 
# 초기 입력
N, K = map(int, input().split()) # N: 동전 종류, K: 목표 가치
coin = [int(input()) for _ in range(N)]
dp = [1] + [0] * K

for i in coin:
    for j in range(i, K+1):
        if j >= i:
            dp[j] += dp[j-i]
print(dp[K])
