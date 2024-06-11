import sys
import math
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
ans = 0

def div(x):
    ret = 1
    for i in range(2, int(math.sqrt(x))+1):
        cnt = 0
        while (x % i == 0):
            cnt += 1
            x /= i
        if not cnt:
            ret *= i
    return int(math.sqrt(M / (ret*x)))

for i in range(1, N+1):
    ans += div(i)

print(ans)