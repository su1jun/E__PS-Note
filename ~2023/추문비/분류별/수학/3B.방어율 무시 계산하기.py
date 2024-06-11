import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
DFB = 0

for i in arr:
    DFB = 1-(1-DFB)*(1-i/100)
    print(round(DFB*100, 6))