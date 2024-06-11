import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(N+1)]
    dp[1][0] = arr1[0]
    dp[1][1] = arr2[0]

    for i in range(2, N+1):
        dp[i][0] = max(max(dp[i-2]) + arr1[i-1], dp[i-1][1] + arr1[i-1])
        dp[i][1] = max(max(dp[i-2]) + arr2[i-1], dp[i-1][0] + arr2[i-1])
    print(max(dp[-1]))