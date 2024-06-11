<<<<<<< HEAD
# 연구소
input = __import__('sys').stdin.readline
from collections import deque
import copy
from itertools import combinations

def bfs(graph):
    que = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                que.append([i, j])

    while que:
        px, py = que.popleft()
        for ix, iy in step:
            nx = ix + px
            ny = iy + py

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                que.append([nx, ny])

    cnt = 0
    for i in range(N):
        cnt += graph[i].count(0)
    return cnt

def backtracking():
    global ans
    ablewall = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                ablewall.append((i, j))
    for wall_combi in combinations(ablewall, 3):
        tmp_graph = copy.deepcopy(graph)
        for i, j in wall_combi:
            tmp_graph[i][j] = 1
            ans = max(bfs(tmp_graph), ans)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
backtracking()

=======
# 연구소
input = __import__('sys').stdin.readline
from collections import deque
import copy
from itertools import combinations

def bfs(graph):
    que = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                que.append([i, j])

    while que:
        px, py = que.popleft()
        for ix, iy in step:
            nx = ix + px
            ny = iy + py

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                que.append([nx, ny])

    cnt = 0
    for i in range(N):
        cnt += graph[i].count(0)
    return cnt

def backtracking():
    global ans
    ablewall = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                ablewall.append((i, j))
    for wall_combi in combinations(ablewall, 3):
        tmp_graph = copy.deepcopy(graph)
        for i, j in wall_combi:
            tmp_graph[i][j] = 1
            ans = max(bfs(tmp_graph), ans)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
backtracking()

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans)