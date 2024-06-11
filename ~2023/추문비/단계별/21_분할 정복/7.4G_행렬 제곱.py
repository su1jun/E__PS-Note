import sys
input = sys.stdin.readline

N, B = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

C = 1000

def f(a, n):
    if n > 1:
        tmp = f(a,n//2)
        m = [[0 for _ in range(N)] for _ in range(N)]

        # 매개 행렬(m) 계산
        for i in range(N):
                for j in range(N):
                    for k in range(N):
                        m[i][j] += tmp[i][k] * tmp[k][j] % C
                        m[i][j] %= C

        if n % 2 == 0:
            return m
        else:
            # 매개 행렬(m*a=ma) 계산
            ma = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        ma[i][j] += m[i][k] * a[k][j] % C
                        ma[i][j] %= C
            return ma
    else:
        for i in range(N):
            for j in range(N):
                a[i][j] %= C
        return a

ans = f(A, B)
for i in range(N):
    print(*ans[i])