import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 101
dp[0] = dp[1] = dp[2] = 1
dp[3] = dp[4] = 2
for i in range(5, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    n = int(input())
    print(dp[n-1])

# for i in range(1, 21):
#     print(f"{i}번째 : {dp[i-1]} ")