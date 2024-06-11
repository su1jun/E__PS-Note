import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N**2)]

for order in range(N**2):
    student = students[order]
    tmp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]

res = 0
students.sort()

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            res += 10 ** (ans-1)
print(res)