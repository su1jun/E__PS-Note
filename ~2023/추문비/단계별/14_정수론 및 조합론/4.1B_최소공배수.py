import sys

T = int(sys.stdin.readline())

def GCD(a, b):
    if a == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return GCD(b, a%b)

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A * B // GCD(A, B))