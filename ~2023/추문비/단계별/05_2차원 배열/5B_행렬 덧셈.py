import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_matrix = [list(map(int, input().split())) for _ in range(N)]
B_matrix = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        ans[i][j] = A_matrix[i][j] + B_matrix[i][j]
for i in ans:
    print(*i)