import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

for i in range(N): # 빨간 구슬과 파란 구슬의 위치 저장
    for j in range(M):
        if graph[i][j] == 'R': rx, ry = i, j
        elif graph[i][j] == 'B': bx, by = i, j

visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 방문 여부 저장
# 위치 초기화
q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = 1

def move(x, y, dx, dy): # 더 이상 움직이지 못할 때까지 이동
    count = 0

    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1

    return x, y, count

def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10: break # 실패 조건

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if graph[nbx][nby] != 'O': # 파란 구슬이 안빠졌을 때
                if graph[nrx][nry] == 'O': # 빨간 구슬만 빠졌으면
                    return depth
                if nrx == nbx and nry == nby: # 두 구슬이 겹치면
                    if rcnt > bcnt: # 더 많이 움직인 구슬을 한 칸 뒤로
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]: # bfs 진행
                    visited[nrx][nry][nbx][nby] = 1
                    q.append([nrx, nry, nbx, nby, depth + 1])
    return -1

print(bfs())