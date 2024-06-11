# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    que = deque([(x)])
    visited[x] = 1
    while que:
        px = que.popleft()
        if px == K:
            return visited[px] - 1
        for i in (px-1, px+1, 2*px):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[px] + 1
                que.append(i)

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]
print(bfs(N))