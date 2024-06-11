<<<<<<< HEAD
# 치즈
from collections import deque
input = __import__('sys').stdin.readline

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0: q.append((nx, ny))
                elif cheeze[nx][ny] == 1: melt.append((nx, ny))
                    
    for x, y in melt:
        cheeze[x][y] = 0
    return len(melt)

N, M = map(int, input().split())
cheeze = []
cnt = 0
for i in range(N):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * M for _ in range(N)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:
        print(time, meltCnt, sep='\n')
        break
=======
# 치즈
from collections import deque
input = __import__('sys').stdin.readline

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0: q.append((nx, ny))
                elif cheeze[nx][ny] == 1: melt.append((nx, ny))
                    
    for x, y in melt:
        cheeze[x][y] = 0
    return len(melt)

N, M = map(int, input().split())
cheeze = []
cnt = 0
for i in range(N):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * M for _ in range(N)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0:
        print(time, meltCnt, sep='\n')
        break
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
    time += 1