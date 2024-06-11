# import sys
# input = sys.stdin.readline

# a = list(input().rstrip())
# b = list(input().rstrip())
# al = len(a)
# bl = len(b)
# dp = [[0] * (bl+1) for _ in range(al+1)]
# for i in range(al):
#     for j in range(bl):
#         if a[i] == b[j]:
#             dp[i+1][j+1] = dp[i][j] + 1
#         else:
#             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
# print(dp[al][bl])

import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
l1, l2 = len(a), len(b)
dp = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif a[i] == b[j]:
            dp[j] = cnt + 1
print(max(dp))