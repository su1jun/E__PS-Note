import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rect = [[0 for _ in range(M+1)]]
for _ in range(N):
    rect.append([0] + list(map(int, list(input().rstrip()))))
 
ans = 0
prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + rect[i][j]
 
def sum_cast(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
 
 
# 1. 세로로만 분할한 경우
for i in range(1, M-1):
    for j in range(i+1, M):
        r1 = sum_cast(1, 1, N, i)
        r2 = sum_cast(1, i+1, N, j)
        r3 = sum_cast(1, j+1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
 
# 2. 가로로만 분할한 경우
for i in range(1, N-1):
    for j in range(i+1, N):
        r1 = sum_cast(1, 1, i, M)
        r2 = sum_cast(i+1, 1, j, M)
        r3 = sum_cast(j+1, 1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 3. 전체 세로 > 우측 가로
for i in range(1, M):
    for j in range(1, N):
        r1 = sum_cast(1, 1, N, i)
        r2 = sum_cast(1, i+1, j, M)
        r3 = sum_cast(j+1, i+1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 4. 전체 세로 > 좌측 가로
for i in range(1, N):
    for j in range(1, M):
        r1 = sum_cast(1, 1, i, j)
        r2 = sum_cast(i+1, 1, N, j)
        r3 = sum_cast(1, j+1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 5. 전체 가로 > 하단 세로
for i in range(1, N):
    for j in range(1, M):
        r1 = sum_cast(1, 1, i, M)
        r2 = sum_cast(i+1, 1, N, j)
        r3 = sum_cast(i+1, j+1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
# 6. 전체 가로 > 상단 세로
for i in range(1, N):
    for j in range(1, M):
        r1 = sum_cast(1, 1, i, j)
        r2 = sum_cast(1, j+1, i, M)
        r3 = sum_cast(i+1, 1, N, M)
        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3
 
print(ans)