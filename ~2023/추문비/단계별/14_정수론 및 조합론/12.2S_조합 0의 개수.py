import sys

N, K = map(int, sys.stdin.readline().split())
def m2(n):
    cnt = 0
    while n != 0:
        n //= 2
        cnt += n
    return cnt

def m5(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

a = m2(N) - m2(K) - m2(N-K)
b = m5(N) - m5(K) - m5(N-K)

print(min(a, b))
