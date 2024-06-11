import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
A %= C
ans = 1

def f(a, n):
    if n > 1:
        tmp = f(a,n//2)
        if n % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * a) % C
    else:
        return a % C
print(f(A, B))