<<<<<<< HEAD
input = __import__('sys').stdin.readline

# union find
def find(x):
    if parent[x] < 0: return x
    parent[x] = find(parent[x]) 
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return
    
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

# ccw
def ccw(x1, y1, x2, y2, x3, y3):
    result = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

    if result > 0: return 1
    elif result == 0: return 0
    else: return -1

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    # 겹칠때
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return 1
                
    # 반작
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
            return 1 
    return 0

N = int(input())
lines = [[]] + [list(map(int, input().split())) for _ in range(N)]
parent = [-1 for _ in range(N+1)]

for i in range(1, N):
    for j in range(i+1, N+1):
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        if check(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)

cnt, max_value = 0, 0

for i in parent[1:]:
    if i < 0:
        cnt += 1
        max_value = max(max_value, abs(i))

print(cnt)
=======
input = __import__('sys').stdin.readline

# union find
def find(x):
    if parent[x] < 0: return x
    parent[x] = find(parent[x]) 
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return
    
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

# ccw
def ccw(x1, y1, x2, y2, x3, y3):
    result = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

    if result > 0: return 1
    elif result == 0: return 0
    else: return -1

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    # 겹칠때
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return 1
                
    # 반작
    elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
            return 1 
    return 0

N = int(input())
lines = [[]] + [list(map(int, input().split())) for _ in range(N)]
parent = [-1 for _ in range(N+1)]

for i in range(1, N):
    for j in range(i+1, N+1):
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        if check(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)

cnt, max_value = 0, 0

for i in parent[1:]:
    if i < 0:
        cnt += 1
        max_value = max(max_value, abs(i))

print(cnt)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(max_value)