from itertools import combinations
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
for i in range(2, N+1):
    temp = list(combinations(arr, i))

    for sp in temp:
        if L <= sum(sp) <= R and max(sp) - min(sp) >= X:
            res += 1

print(res)