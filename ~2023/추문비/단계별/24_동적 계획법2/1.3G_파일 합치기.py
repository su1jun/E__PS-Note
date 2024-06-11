import sys
input = sys.stdin.readline

# 초기 설정
T = int(input())
for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))

    sdata = [0]
    for i in range(K):
        sdata.append(sdata[-1] + data[i])
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    # 계산 진행 
    for i in range(1, K): # i = len
        for j in range(1, K-i+1): # j = 행렬 계산 반복횟수
            m = 1e9
            for k in range(i): # k = 최소값 계산 반복횟수
                a = dp[j][j+k] + dp[j+k+1][j+i]
                if m > a:
                    m = a
            dp[j][j+i] = (sdata[j+i] - sdata[j-1]) + m
    print(dp[1][K])

from math import inf

# for t in range(int(input())):
#     n = int(input())
#     arr = tuple(map(int, input().split()))

#     prefix = [0]
#     for i in range(n):
#         prefix.append(prefix[-1]+arr[i])

#     dp = [[inf] * (n+1) for _ in range(n+1)]
#     dpk = [[0] * n for _ in range(n)]
#     for i in range(n):
#         dp[i][i] = 0
#         dpk[i][i] = i

#     for d in range(1, n):
#         for i in range(n-d):
#             j = i+d
#             for k in range(dpk[i][j-1], dpk[i+1][j]+1):
#                 if dp[i][j] > dp[i][k]+dp[k+1][j]:
#                     dpk[i][j] = k
#                     dp[i][j] = dp[i][k]+dp[k+1][j]
#             dp[i][j] += prefix[j+1]-prefix[i]

#     print(dp[0][-2])