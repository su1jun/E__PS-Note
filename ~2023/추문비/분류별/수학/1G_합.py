import sys
input = sys.stdin.readline

def cal(x, ans, point):
    while x > 0:
        ans[x % 10] += point
        x //= 10

def fic(end):
    ans = [0] * 10
    point = 1
    start = 1
    while start <= end:
        while end % 10 != 9:
            cal(end, ans, point)
            end -= 1
        if end < start:
            break
        while start % 10 != 0:
            cal(start, ans, point)
            start += 1
        start //= 10
        end //= 10
        for i in range(10):
            ans[i] += (end - start + 1) * point
        point *= 10
    sum = 0
    for i in range(10):
        sum += i * ans[i]
    return sum

L, U = map(int, input().split())

print(fic(U) - fic(L-1))