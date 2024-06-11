import sys
input = sys.stdin.readline
 
# 초기 입력
N, K = map(int, input().split()) # N: 동전 종류, K: 목표 가치
coin = set([int(input()) for _ in range(N)])
dp = [0] + [10001] * (K)

for num in coin:
   for i in range(num, K+1):
       dp[i] = min(dp[i], dp[i-num]+1)
if dp[K] == 10001:
   print(-1)
else:
   print(dp[K])