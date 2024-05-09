import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(x, y):
    cnt = 0
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if graph[nx][ny] !="X":
                    visited[nx][ny] = True
                    if graph[nx][ny] == "P": cnt += 1
                    q.append((nx, ny))

    return cnt

dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M = map(int,input().split())
graph = list(input() for _ in range(N))
visited = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j]=="I":
            cnt = bfs(i,j)
            break

if cnt==0:
    print("TT")
else:
    print(cnt)