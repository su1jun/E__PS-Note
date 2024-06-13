input = __import__('sys').stdin.readline

N = int(input())
Arr = [0] + list(map(int, input().split()))

dp = [-1] * 101
dp[Arr[1]] = 0

for i in range(2, N+1):
    for j in range(1, 101):
        if dp[j] != -1:
            dp[Arr[i]] = max(dp[Arr[i]], dp[j] + (Arr[i] - j)**2)

print(max(dp))