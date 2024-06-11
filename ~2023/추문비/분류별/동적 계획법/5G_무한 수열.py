import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(n):
    if data[n] != 0:
        return data[n]

    data[n] = dfs(n // P) + dfs(n // Q)
    return data[n]

N, P, Q = map(int, input().split())
data = defaultdict(int)
data[0] = 1

print(dfs(N))