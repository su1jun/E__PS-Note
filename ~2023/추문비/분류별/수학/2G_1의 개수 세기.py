import sys
input = sys.stdin.readline

def clc(n):
    cnt = 0
    binary = bin(n)[2:]
    length = len(binary)

    for i in range(length):
        if binary[i] == '1':
            pow = length - i - 1
            cnt += Prefix[pow]
            cnt += (n - 2 ** pow + 1)
            n = n - 2 ** pow
    return cnt

A, B = map(int, input().split())
Prefix = [0] * 60

for i in range(1, 60):
    Prefix[i] = 2 ** (i-1) + 2 * Prefix[i-1]

print(clc(B) - clc(A-1))