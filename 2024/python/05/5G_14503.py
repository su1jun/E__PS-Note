import sys
input = sys.stdin.readline

N, M = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

def clean(x, y, d):
    global cnt
    
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

    for i in range(3, -1, -1):
        nd = (d+i)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return
    
    bx = x - dx[d]
    by = y - dy[d]
    if 0 <= bx < N and 0 <= by < M:
        if graph[bx][by] == 1:
            return
        else:
            clean(bx, by, d)

clean(r,c,d)
print(cnt)
