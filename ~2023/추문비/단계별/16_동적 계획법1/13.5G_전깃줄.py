import sys
input = sys.stdin.readline

N = int(input())
nums = []
dp = [0] * 501
mini = 0
for _ in range(N):
    nums.append(list(map(int, input().split())))
nums.sort(key=lambda x : (x[0]))
for i in nums:
    a = max(dp[:i[1]])+1
    dp[i[1]] = a
    if mini < a:
        mini = a
print(N-mini)