import sys

N, K = map(int, sys.stdin.readline().split())

def bino(n, k):
    if n == k or k == 0:
        return 1
    else:
        return bino(n-1, k-1) + bino(n-1, k)
print(bino(N, K))
