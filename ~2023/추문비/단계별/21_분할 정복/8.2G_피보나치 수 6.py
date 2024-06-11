import sys
input = sys.stdin.readline

N = int(input())
m = [[1, 1], [1, 0]]
C = 1000000007

def multiply(a, b): # 행렬곱
    m = []
    for i in range(len(a)):
        m.append([])
        for j in range(len(b[0])):
            tmp = 0
            for k in range(len(a[0])):
                tmp += a[i][k] * b[k][j]
            m[i].append(tmp % C)
    return m

def f(a, n): # 분할
    if n > 1:
        tmp = f(a, n//2)
        if n % 2 == 0:
            return multiply(tmp, tmp)
        else:
            return multiply(multiply(tmp, tmp), a)
    else:
        return a

print(f(m, N)[0][1])