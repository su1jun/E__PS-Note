import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
S = 0
for _ in range(N):
    a, b = map(int, input().split())
    S += a*b 
if S == X:
    print("Yes")
else:
    print("No")