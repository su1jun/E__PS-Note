from collections import defaultdict
input = __import__('sys').stdin.readline

def dfs(n):
    pass

N = int(input())
graph = defaultdict(list)
for i in range(1, N+1):
    graph[int(input())].append(i)