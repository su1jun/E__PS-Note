import sys
input = sys.stdin.readline

n = int(input())
dp1 = []

for _ in range(n):
    dp1.append(int(input()))

if n == 1:
    print(dp1[0])

else:
    dp2 = dp1.copy()
    dp2[1] += dp2[0]
    # print(f"dp1 : {dp1}")
    # print(f"dp2 : {dp2}")
    for i in range(2, n):
        if i % 2 == 0:
            dp1[i] += dp1[i-1]
            dp2[i] += max(dp1[i-2], dp2[i-2])
            # print(f"{i}/dp1 : {dp1}")
            # print(f"{i}/dp2 : {dp2}")
        else:
            dp1[i] += max(dp1[i-2], dp2[i-2])
            dp2[i] += dp2[i-1]
            # print(f"{i}/dp1 : {dp1}")
            # print(f"{i}/dp2 : {dp2}")
    print(max(dp1[-1], dp2[-1]))

###
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])