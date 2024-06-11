import sys
input = sys.stdin.readline

T, W = map(int, input().rsplit())
exloc = 0
arr = [0]
for _ in range(T):
    loc = int(input()) - 1
    if exloc != loc:
        exloc = loc
        arr.append(1)
    else:
        arr[-1] += 1

T = len(arr)

dp = [[0 for _ in range(T)] for _ in range(W+1)]

dp[0][0] = arr[0]
for i in range(2, T, 2):
    dp[0][i] = arr[i] + dp[0][i-2]

for i in range(1, W+1):
    if T > 1 and i % 2 == 1:
        dp[i][1] = arr[1] + arr[0]
        for j in range(3, T, 2):
            dp[i][j] = arr[j] + max(dp[i][j-2], dp[i-1][j-1])
    else:
        dp[i][0] = arr[0]
        for j in range(2, T, 2):
            dp[i][j] = arr[j] + max(dp[i][j-2], dp[i-1][j-1])
ans = 0
for i in range(W+1):
    ans = max(ans, dp[i][-1])
print(ans)
# for i in range(W+1):
#     print(dp[i])