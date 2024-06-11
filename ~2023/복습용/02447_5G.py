input = __import__('sys').stdin.readline

def rec(n):
    if n == 1: return ["*"]

    tmp = rec(n//3)
    res = []

    for i in tmp: res.append(i * 3)
    for i in tmp: res.append(i + ' '*(n//3) + i)
    for i in tmp: res.append(i * 3)

    return res

N = int(input())
print('\n'.join(rec(N)))