import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        arr.append(int("".join(map(str, comb))))
arr.sort()

try:
    print(arr[N])
except:
    print(-1)