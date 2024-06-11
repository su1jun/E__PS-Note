import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N) for _ in range(N)]
for _ in range(M):
    v, e = map(int, input().split())
    arr[v-1][e-1] = 1

for path in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][path] == 1 and arr[path][j] == 1:
                arr[i][j] = 1
ans = 0
for i in range(N):
    chk = 0
    for j in range(N):
        chk += arr[i][j] + arr[j][i]
    if chk == N - 1:
        ans += 1
print(ans)