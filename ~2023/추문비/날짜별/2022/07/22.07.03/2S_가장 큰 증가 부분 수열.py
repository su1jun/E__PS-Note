import sys
n = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001

for i in As:
    dp[i] = max(dp[:i])+i
print(max(dp))