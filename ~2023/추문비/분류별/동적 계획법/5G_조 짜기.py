import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i]
    min_ = max_ = arr[i]
    j = i-1
    while j >= 0 and (arr[j] < min_ or arr[j] > max_):
        min_, max_ = min(arr[j], min_), max(arr[j], max_)
        dp[i+1] = max(dp[i+1], dp[j] + max_ - min_)
        j -= 1

print(dp[-1])