<<<<<<< HEAD
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
digits = [0] * 19
cache = [[[0] * 2 for _ in range(19)] for _ in range(1<<11)]
L = 0
p = 0

def calDigist():
    global L
    num = N

    while num > 0:
        digits[L] = num % 10
        L += 1
        num //= 10

    for e in range(L-1):
        pass
=======
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
digits = [0] * 19
cache = [[[0] * 2 for _ in range(19)] for _ in range(1<<11)]
L = 0
p = 0

def calDigist():
    global L
    num = N

    while num > 0:
        digits[L] = num % 10
        L += 1
        num //= 10

    for e in range(L-1):
        pass
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
    