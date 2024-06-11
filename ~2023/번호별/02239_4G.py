<<<<<<< HEAD
import sys
input = sys.stdin.readline

graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blank = []

for i, j in [(x, y) for x in range(9) for y in range(9)]:
    if graph[i][j] == 0: blank.append((i, j))

def chkRow(x, d):
    for i in range(9):
        if d == graph[x][i]: return False
        return True
    
def chkCol(y, d):
    for i in range(9):
        if d == graph[i][y]: return False
        return True
    
def chkRect(x, y, d):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i, j in [(x, y) for x in range(3) for y in range(3)]:
        if d == graph[nx+i][ny+j]: return False
        return True
    
def dfs(n):
    if n == len(blank):
        for i in graph:
            print("".join(list(map(str, i))))
        exit(0)

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if chkRow(x, i) and chkCol(x, i) and chkRect(x, y, i):
            graph[x][y] = 1
            dfs(n+1)
            graph[x][y] = 0

=======
import sys
input = sys.stdin.readline

graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blank = []

for i, j in [(x, y) for x in range(9) for y in range(9)]:
    if graph[i][j] == 0: blank.append((i, j))

def chkRow(x, d):
    for i in range(9):
        if d == graph[x][i]: return False
        return True
    
def chkCol(y, d):
    for i in range(9):
        if d == graph[i][y]: return False
        return True
    
def chkRect(x, y, d):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i, j in [(x, y) for x in range(3) for y in range(3)]:
        if d == graph[nx+i][ny+j]: return False
        return True
    
def dfs(n):
    if n == len(blank):
        for i in graph:
            print("".join(list(map(str, i))))
        exit(0)

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if chkRow(x, i) and chkCol(x, i) and chkRect(x, y, i):
            graph[x][y] = 1
            dfs(n+1)
            graph[x][y] = 0

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
dfs(0)