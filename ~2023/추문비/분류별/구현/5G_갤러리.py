import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(input()))
hap = 0
CP_ru = [ [0] * M for _ in range(N)]
CP_rd = [ [0] * M for _ in range(N)]
CP_ur = [ [0] * M for _ in range(N)]
CP_ul = [ [0] * M for _ in range(N)]

def chk(y,x):
    global arr
    global hap
    if arr[y][x] == ".":
        if arr[y+1][x] == ".":
            if arr[y][x-1] == "X" and arr[y+1][x-1] == "X" and CP_ul[y][x] == 0:
                CP_ul[y][x] = 1
                CP_ul[y+1][x] = 1
                hap += 1
            if arr[y][x+1] == "X" and arr[y+1][x+1] == "X" and CP_ur[y][x] == 0:
                CP_ur[y][x] = 1
                CP_ur[y+1][x] = 1
                hap += 1
        if arr[y][x+1] == ".":
            if arr[y-1][x] == "X" and arr[y-1][x+1] == "X" and CP_ru[y][x] == 0:
                CP_ru[y][x] = 1
                CP_ru[y][x+1] = 1
                hap += 1
            if arr[y+1][x] == "X" and arr[y+1][x+1] == "X" and CP_rd[y][x] ==0:
                CP_rd[y][x] = 1
                CP_rd[y][x+1] = 1
                hap += 1

for i in range(1, N-1):
    for t in range(1, M-1):
        chk(i, t)
print(hap)