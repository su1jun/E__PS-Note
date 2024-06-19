import sys, math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())

Answer_T = sum([math.ceil(i / T) for i in arr])
Answer_P = (N // P, N % P)
print(Answer_T)
print(*Answer_P)