<<<<<<< HEAD
import sys
from collections import deque
input = sys.stdin.readline

letter = ''

def bfs(Sp):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([Sp])
    check[Sp[0]][Sp[1]] = '.'

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and check[nx][ny] == '#' and Mat[nx][ny] == letter:
                queue.append((nx, ny))
                check[nx][ny] = '.'

def move(Str,Start):
    global letter
    coords=[Start[0]-1,Start[1]-1]

    for i in Str:
        if i=='U':
            coords = [coords[0]-1, coords[1]]
        elif i=='D':
            coords = [coords[0]+1, coords[1]]
        elif i=='L':
            coords = [coords[0], coords[1]-1]
        elif i=='R':
            coords = [coords[0], coords[1]+1]
        elif i=='W':
            letter = Mat[coords[0]][coords[1]]
            bfs(coords)
    a,b=coords[0],coords[1]

    check[a][b] = '.'
    if a>0:
        check[a-1][b] = '.'
    if a<R-1:
        check[a+1][b] = '.'
    if b<C-1:
        check[a][b+1] = '.'
    if b>0:
        check[a][b-1] = '.'

    return check

R,C=map(int,input().split())

Mat=[list(input()) for _ in range(R)]

check=[["#"]*C for _ in range(R)]

start=list(map(int,input().split()))

str = input()

move(str, start)

for i in check:
=======
import sys
from collections import deque
input = sys.stdin.readline

letter = ''

def bfs(Sp):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([Sp])
    check[Sp[0]][Sp[1]] = '.'

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and check[nx][ny] == '#' and Mat[nx][ny] == letter:
                queue.append((nx, ny))
                check[nx][ny] = '.'

def move(Str,Start):
    global letter
    coords=[Start[0]-1,Start[1]-1]

    for i in Str:
        if i=='U':
            coords = [coords[0]-1, coords[1]]
        elif i=='D':
            coords = [coords[0]+1, coords[1]]
        elif i=='L':
            coords = [coords[0], coords[1]-1]
        elif i=='R':
            coords = [coords[0], coords[1]+1]
        elif i=='W':
            letter = Mat[coords[0]][coords[1]]
            bfs(coords)
    a,b=coords[0],coords[1]

    check[a][b] = '.'
    if a>0:
        check[a-1][b] = '.'
    if a<R-1:
        check[a+1][b] = '.'
    if b<C-1:
        check[a][b+1] = '.'
    if b>0:
        check[a][b-1] = '.'

    return check

R,C=map(int,input().split())

Mat=[list(input()) for _ in range(R)]

check=[["#"]*C for _ in range(R)]

start=list(map(int,input().split()))

str = input()

move(str, start)

for i in check:
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
    print("".join(i))