<<<<<<< HEAD
import sys
import math
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
K = int(input())
R = [[(j*10**len(str(S[i])) + S[i])%K for j in range(K)] for i in range(N)]
dp = [[0] * K for _ in range(1<<N)]
dp[0][0] = 1

for b in range(1<<N):
    for i in range(N):
        if b & (1<<i): continue
        for j in range(K):
            dp[b|(1<<i)][R[i][j]] += dp[b][j]
p = dp[(1<<N) - 1][0]
q = sum(dp[(1<<N) - 1])
g = math.gcd(p, q)
=======
import sys
import math
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]
K = int(input())
R = [[(j*10**len(str(S[i])) + S[i])%K for j in range(K)] for i in range(N)]
dp = [[0] * K for _ in range(1<<N)]
dp[0][0] = 1

for b in range(1<<N):
    for i in range(N):
        if b & (1<<i): continue
        for j in range(K):
            dp[b|(1<<i)][R[i][j]] += dp[b][j]
p = dp[(1<<N) - 1][0]
q = sum(dp[(1<<N) - 1])
g = math.gcd(p, q)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print("%d/%d"%(p//g,q//g))