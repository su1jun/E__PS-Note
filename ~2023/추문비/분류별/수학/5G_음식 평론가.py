import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
    
N, M = map(int, input().split())
print(M - gcd(N, M))