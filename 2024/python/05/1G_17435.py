import sys
input = sys.stdin.readline

M = int(input())
f = [0] + list(map(int, input().split()))
dp = [[f[i]] for i in range(M + 1)]

for i in range(1, 19):
    for j in range(1, M + 1):
        dp[j].append(dp[dp[j][i-1]][i-1])

for _ in range(int(input())):
    N, X = map(int, input().split())

    for i in range(18, -1, -1):
        if N >= 1 << i:
            N -= 1 << i
            X = dp[X][i]

    print(X)