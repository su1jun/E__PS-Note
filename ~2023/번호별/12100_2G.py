<<<<<<< HEAD
from collections import deque
input = __import__('sys').stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer, que = 0, deque()

def get(i, j):
    if board[i][j]: # 0이 아닌 값이라면
        que.append(board[i][j]) # queueue에 board의 값을 넣는다.
        board[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트
        
def merge(i, j, di, dj): # row index, column index, y방향, x방향 
    while que:
        x = que.popleft() # 움직이려는 블록 값을 가져온다. FIFO 
        if not board[i][j]: # 0이라면 그대로 놓는다.
            board[i][j] = x
        elif board[i][j] == x: # 값이 일치한다면
            board[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj 
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj
            board[i][j] = x 

def move(k):
    # board[i][j]
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
    elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
    elif k == 2: # 오른쪽으로 이동, column index는 0
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
    else: # 왼쪽으로 이동, column index는 n-1
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동
            
def solve(count):
    global board, answer
    if count == 5: # 최대 5번까지 움직였다면
        for i in range(N):
            answer = max(answer, max(board[i])) # 가장 큰 값이 answer
        return
    b = [x[:] for x in board] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
    
    for k in range(4): # 4방향으로 움직인다.
        move(k) # 움직인다.
        solve(count+1) # 재귀적으로 호출한다.
        board = [x[:] for x in b]

solve(0)
=======
from collections import deque
input = __import__('sys').stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer, que = 0, deque()

def get(i, j):
    if board[i][j]: # 0이 아닌 값이라면
        que.append(board[i][j]) # queueue에 board의 값을 넣는다.
        board[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트
        
def merge(i, j, di, dj): # row index, column index, y방향, x방향 
    while que:
        x = que.popleft() # 움직이려는 블록 값을 가져온다. FIFO 
        if not board[i][j]: # 0이라면 그대로 놓는다.
            board[i][j] = x
        elif board[i][j] == x: # 값이 일치한다면
            board[i][j] = x*2 # 합쳐지므로 2배로 증가
            i, j = i+di, j+dj 
        else: # 값이 일치하지 않으면
            i, j = i+di, j+dj
            board[i][j] = x 

def move(k):
    # board[i][j]
    if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
    elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
        for j in range(N):
            for i in range(N-1, -1, -1):
                get(i, j)
            merge(N-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
    elif k == 2: # 오른쪽으로 이동, column index는 0
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
    else: # 왼쪽으로 이동, column index는 n-1
        for i in range(N):
            for j in range(N-1, -1, -1):
                get(i, j)
            merge(i, N-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동
            
def solve(count):
    global board, answer
    if count == 5: # 최대 5번까지 움직였다면
        for i in range(N):
            answer = max(answer, max(board[i])) # 가장 큰 값이 answer
        return
    b = [x[:] for x in board] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
    
    for k in range(4): # 4방향으로 움직인다.
        move(k) # 움직인다.
        solve(count+1) # 재귀적으로 호출한다.
        board = [x[:] for x in b]

solve(0)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(answer)