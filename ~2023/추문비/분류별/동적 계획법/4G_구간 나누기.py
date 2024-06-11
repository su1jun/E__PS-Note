# n-1을 포함 vs n-1을 미포함
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp1 = [[0] + [-1e9] * M for _ in range(N+1)] # [i] 포함
dp2 = [[0] + [-1e9] * M for _ in range(N+1)] # [i] 미포함

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min(M, (i+1)//2)+1):
        dp2[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j-1]) + num
print(max(dp2[N][M], dp1[N][M]))