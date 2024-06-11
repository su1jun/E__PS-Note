import sys
input = sys.stdin.readline

n = int(input())
s = [0 for _ in range(10001)]
dp = [0 for _ in range(10001)]

for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i], dp[i-1])
print(dp[n-1])
