import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(n):
    if n <= 0:
        return 1

    if data[n] != 0:
        return data[n]

    data[n] = dfs(n // P - X) + dfs(n // Q - Y)
    return data[n]

N, P, Q, X, Y = map(int, input().split())
data = defaultdict(int)
data[0] = 1

print(dfs(N))