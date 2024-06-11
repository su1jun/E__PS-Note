import sys
input = sys.stdin.readline

N = int(input())
Perfix = [[-1001]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(1, N+1):
        Perfix[i][j] = Perfix[i][j-1] + Perfix[i-1][j] - Perfix[i-1][j-1] + arr[j-1]

max_fit = Perfix[0][0]
for k in range(N):
    for i in range(1, N-k+1):
        for j in range(1, N-k+1):
            tmp = Perfix[i+k][j+k] - Perfix[i-1][j+k] - Perfix[i+k][j-1] + Perfix[i-1][j-1]
            if tmp > max_fit:
                max_fit = tmp
print(max_fit)