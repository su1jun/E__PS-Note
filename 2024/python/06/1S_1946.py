import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    dp = [0] * (N + 1)
    ans = 1

    for _ in range(N):
        T1, T2 = map(int, input().split())
        dp[T1] = T2

    min_val = dp[1]
    for i in range(2, N+1):
        if dp[i] < min_val:
            min_val = dp[i]
            ans += 1

    print(ans)

# 0 4 3 2 1 5

# 0 4 5 6 2 7 1 3