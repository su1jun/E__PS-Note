import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
minimap = [input().rstrip() for _ in range(M)]
prefix_J = [[0] * (N+1) for _ in range(M+1)]
prefix_O = [[0] * (N+1) for _ in range(M+1)]
prefix_I = [[0] * (N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        tmp = minimap[i-1][j-1]
        if tmp == "J":
            prefix_J[i][j] += 1
        elif tmp == "O":
            prefix_O[i][j] += 1
        else:
            prefix_I[i][j] += 1
        prefix_J[i][j] += prefix_J[i-1][j] + prefix_J[i][j-1] - prefix_J[i-1][j-1]
        prefix_O[i][j] += prefix_O[i-1][j] + prefix_O[i][j-1] - prefix_O[i-1][j-1]
        prefix_I[i][j] += prefix_I[i-1][j] + prefix_I[i][j-1] - prefix_I[i-1][j-1]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    J = prefix_J[c][d] - prefix_J[a-1][d] - prefix_J[c][b-1] + prefix_J[a-1][b-1]
    O = prefix_O[c][d] - prefix_O[a-1][d] - prefix_O[c][b-1] + prefix_O[a-1][b-1]
    I = prefix_I[c][d] - prefix_I[a-1][d] - prefix_I[c][b-1] + prefix_I[a-1][b-1]
    print(J, O, I)