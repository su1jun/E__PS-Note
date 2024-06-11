import sys
input = sys.stdin.readline
data = []
blank = []

for i in range(9):
    data.append(list(map(int, input().rstrip().split())))

for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            blank.append((i, j))

def chkRow(x, a):
    for i in range(9):
        if a == data[x][i]:
            return False
    return True

def chkCol(y, a):
    for i in range(9):
        if a == data[i][y]:
            return False
    return True

def chkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == data[nx+i][ny+j]:
                return False
    return True


def f(idx):
    if idx == len(blank):
        for i in range(9):
            print(*data[i])
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if chkRow(x, i) and chkCol(y, i) and chkRect(x, y, i):
            data[x][y] = i
            f(idx+1)
            data[x][y] = 0

f(0)