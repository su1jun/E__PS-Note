<<<<<<< HEAD
import sys
input = sys.stdin.readline

N = int(input())
dp = [[[-1] * 11 for _ in range(101)] for _ in range(1 << 11)]
mod = 1000000000

def go(f, b, x):
    if x < 0 or x > 9: return 0
    if b == N:
        if f == (1 << 10) - 1: return 1
        return 0
        
    if dp[f][b][x] != -1: return dp[f][b][x]
    dp[f][b][x] = 0
    if x == 0: dp[f][b][x] += go(f | (1 << (x+1)), b+1, (x+1))
    elif x == 9: dp[f][b][x] += go(f | (1 << (x-1)), b+1, (x-1))
    else: dp[f][b][x] += go(f | (1 << (x+1)), b+1, (x+1)) + go(f | (1 << (x-1)), b+1, (x-1))
    
    dp[f][b][x] %= mod
    return dp[f][b][x]

ans = 0

for i in range(1, 10):
    ans += go(1 << i, 1, i)
    ans %= mod

=======
import sys
input = sys.stdin.readline

N = int(input())
dp = [[[-1] * 11 for _ in range(101)] for _ in range(1 << 11)]
mod = 1000000000

def go(f, b, x):
    if x < 0 or x > 9: return 0
    if b == N:
        if f == (1 << 10) - 1: return 1
        return 0
        
    if dp[f][b][x] != -1: return dp[f][b][x]
    dp[f][b][x] = 0
    if x == 0: dp[f][b][x] += go(f | (1 << (x+1)), b+1, (x+1))
    elif x == 9: dp[f][b][x] += go(f | (1 << (x-1)), b+1, (x-1))
    else: dp[f][b][x] += go(f | (1 << (x+1)), b+1, (x+1)) + go(f | (1 << (x-1)), b+1, (x-1))
    
    dp[f][b][x] %= mod
    return dp[f][b][x]

ans = 0

for i in range(1, 10):
    ans += go(1 << i, 1, i)
    ans %= mod

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans)