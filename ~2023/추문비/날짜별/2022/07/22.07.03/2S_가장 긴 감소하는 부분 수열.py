import sys
n = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1002

for i in As:
    dp[i] = max(dp[i+1:])+1
print(max(dp))