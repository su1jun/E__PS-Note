import sys
import copy
import random
from collections import deque
input = sys.stdin.readline

step1 = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 상하좌우
step2 = [[1, 1], [-1, -1], [-1, 1], [1, -1]] # 대각스탭
dgn_wei = 2 # 대각선 가중치
def bfs(lst):
    que = deque(lst)
    while que:
        px, py = que.popleft()
        for i, j in step1:
            nx = px + i
            ny = py + j
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] > graph[px][py] + 1:
                graph[nx][ny] = graph[px][py] + 1
                que.append((nx, ny))
        for i, j in step2:
            nx = px + i
            ny = py + j
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] > graph[px][py] + dgn_wei:
                graph[nx][ny] = graph[px][py] + dgn_wei
                que.append((nx, ny))

def det_number(arr): # 출력 맞춤용
    tmp = 0
    
    for i in arr:
        for j in i:
            if j != 1e9 and j > tmp:
                tmp = j

    return len(str(tmp))

N, M = map(int, input().split())
K = int(input()) # 장애물 갯수
graph = [[1e9] * N for _ in range(M)] # M : 가로, N : 세로

while K != 0: # 장애물 설치 while문
    a = random.randint(0, M-1)
    b = random.randint(0, N-1)
    if graph[a][b]:
        graph[a][b] = 0
        K -= 1

print("-"*(M//2-1)+"초기 grid"+"-"*(M//2-1)) # 초기 gird 출력
opening = copy.deepcopy(graph)
for i in range(M):
    for j in range(N):
        if opening[i][j] == 1e9:
            opening[i][j] = "0"
        else:
            opening[i][j] = "B"
for i in opening:
    print(*i)

start = [[M-1, N-1]]
graph[M-1][N-1] = 0
bfs(start)

print()
print("-"*(M//2-1)+"완료 grid"+"-"*(M//2-1)) # 처리 gird 출력
l1 = det_number(graph)
finish = copy.deepcopy(graph)
for i in range(M):
    for j in range(N):
        l2 = len(str(finish[i][j]))
        if finish[i][j] == 0:
            finish[i][j] = "B" * l1
        elif finish[i][j] == 1e9:
            finish[i][j] = "X" * l1
        elif l2 < l1:
            finish[i][j] = "0" * (l1 - l2) + str(finish[i][j])
for i in range(M):
    for j in range(N):
        l2 = len(str(finish[i][j]))
        if finish[i][j] == "B":
            finish[i][j] = "B" * l1
        elif finish[i][j] == "X":
            finish[i][j] = "X" * l1
        elif l2 < l1:
            finish[i][j] = "0" * (l1 - l2) + str(finish[i][j])
            
finish[M-1][N-1] = "0" * l1
for i in finish:
    print(*i)