# bfs 방문여부
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)] # M : 가로, N : 세로

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1
    
    step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def bfs(x, y):
        que = deque([(x, y)])
        graph[x][y] = 0

        while que:
            px, py = que.popleft()
            for i, j in step:
                nx = px + i
                ny = py + j
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    que.append((nx, ny))
        return # <<<< ㅋㅋ 이거땜에 애먹었다

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                bfs(i, j)
                cnt += 1
    
    print(cnt)