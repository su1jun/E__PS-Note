crd = [[[0]for _ in range(100)] for _ in range(100)]

for _ in range(4):
    l_x,l_y,r_x,r_y = map(int, input().split())
    for i in range(l_x, r_x):
        for j in range(l_y, r_y):
            crd[i][j] = 1
        
cnt = 0

for m in range(100):
    for n in range(100):
        if crd[m][n] == 1:
            cnt += 1

print(cnt)
