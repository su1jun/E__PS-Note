import sys
import math
input = sys.stdin.readline

N = int(input())
p = 1000000007

cnt = N
ans = 0
for i in range(N+4, N*5+1, 4):
    cnt -= 1
    if i % 3 == 0:
        #print(i, cnt)
        ans += math.comb(N-1, cnt) % p
print(ans % p)
