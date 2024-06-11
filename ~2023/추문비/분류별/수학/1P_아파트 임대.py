import sys
input = sys.stdin.readline

# 밀러 라빈 n - 1 = d x 2^s
def f(n, a):
    d = (n - 1) // 2

    while (d % 2 == 0):
        if (pow(a, d, n) == n-1):
            return True
        d //= 2
    
    tmp = pow(a, d, n)
    if tmp == n-1 or tmp == 1:
        return True
    else:
        return False

N = int(input())

lst = [2, 7, 61] # 체크리스트
cnt = 0
for _ in range(N):
    n = int(input())*2 + 1 # 판별 수

    for i in lst:
        if not f(n, i):
            if n in lst: # 예외처리
                cnt += 1
            break
    else:
        cnt += 1

print(cnt)
