<<<<<<< HEAD
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    cnt = 1
    while que:
        i, j = que.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            que.append((ni, nj))
            cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
zeros = [[0] * M for _ in range(N)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(N):
    for j in range(M):
        aList = set()
        if graph[i][j]:
            for dtx, dty in zip(dx, dy):
                ni, nj = i + dty, j + dtx
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                aList.add(zeros[ni][nj])
            for add in aList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
=======
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    cnt = 1
    while que:
        i, j = que.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            que.append((ni, nj))
            cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
zeros = [[0] * M for _ in range(N)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(N):
    for j in range(M):
        aList = set()
        if graph[i][j]:
            for dtx, dty in zip(dx, dy):
                ni, nj = i + dty, j + dtx
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                aList.add(zeros[ni][nj])
            for add in aList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
    print("".join(map(str, g)))