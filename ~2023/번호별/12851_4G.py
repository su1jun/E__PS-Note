<<<<<<< HEAD
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    global res
    que = deque()
    que.append(start)
    arr[start] = 0
    
    while que:
        x = que.popleft()
        if x == K:
            res += 1
            continue
        for nx in (x*2, x+1, x-1):
            if 0 <= nx < 100001 and (arr[nx] == arr[x] + 1 or arr[nx] == -1):
                arr[nx] = arr[x] + 1
                que.append(nx)


N, K = map(int, input().split())
arr = [-1] * 100001
res = 0

bfs(N)

print(arr[K])
=======
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    global res
    que = deque()
    que.append(start)
    arr[start] = 0
    
    while que:
        x = que.popleft()
        if x == K:
            res += 1
            continue
        for nx in (x*2, x+1, x-1):
            if 0 <= nx < 100001 and (arr[nx] == arr[x] + 1 or arr[nx] == -1):
                arr[nx] = arr[x] + 1
                que.append(nx)


N, K = map(int, input().split())
arr = [-1] * 100001
res = 0

bfs(N)

print(arr[K])
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(res)