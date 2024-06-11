<<<<<<< HEAD
input = __import__('sys').stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (101) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        cal = dp[j] + (arr[i-1] - arr[j-1]) ** 2
        if dp[i] < cal: dp[i] = cal
    dp[i] = max(dp[i], dp[i-1])
=======
input = __import__('sys').stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (101) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        cal = dp[j] + (arr[i-1] - arr[j-1]) ** 2
        if dp[i] < cal: dp[i] = cal
    dp[i] = max(dp[i], dp[i-1])
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(dp[N])