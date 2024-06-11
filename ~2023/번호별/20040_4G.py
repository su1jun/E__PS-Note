<<<<<<< HEAD
# 사이클 게임
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]: x = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = list(range(N))

for i in range(1, M+1):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i)
        
else:
    print(0)
=======
# 사이클 게임
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]: x = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = list(range(N))

for i in range(1, M+1):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i)
        
else:
    print(0)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
