import sys
input = sys.stdin.readline

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

T = int(input())
for _ in range(T):
    M, N, X, Y = map(int, input().split())
    print(num(M, N, X, Y))