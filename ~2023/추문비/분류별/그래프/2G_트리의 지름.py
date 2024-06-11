import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    visit = [-1] * (V + 1)
    que = deque([node])
    visit[node] = 0
    max_far = [0, 0]

    while que:
        tmp = que.popleft()
        for n, wei in graph[tmp]:
            if visit[n] == -1:
                visit[n] = visit[tmp] + wei
                que.append(n)
                if max_far[0] < visit[n]:
                    max_far = visit[n], n
    return max_far

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)