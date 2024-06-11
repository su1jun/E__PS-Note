import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1]

for i in range(2, N+1):
    m = 1e9
    j = 1

    while (j**2) <= i:
        m = min(m, dp[i-(j**2)])
        j += 1
    dp.append(m + 1)

print(dp[N])