<<<<<<< HEAD
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    que = deque([(N, 0)])
    visited[start] = start
    while que:
        cur, cur_time = que.popleft()
        if cur == target:
            idx = cur
            while idx != start:
                path.append(idx)
                idx = visited[idx]
            path.append(start)
            return cur_time
    
        if cur+1 < 100001 and visited[cur+1] == -1:
            que.append((cur+1, cur_time+1))
            visited[cur+1] = cur
        
        if cur-1 >= 0 and visited[cur-1] == -1:
            que.append((cur-1, cur_time+1))
            visited[cur-1] = cur
        
        if cur*2 < 100001 and visited[cur*2] == -1:
            que.append((cur*2, cur_time+1))
            visited[cur*2] = cur

visited = [-1] * 100001
path = []

N, K = map(int, input().split())

print(bfs(N, K))
=======
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    que = deque([(N, 0)])
    visited[start] = start
    while que:
        cur, cur_time = que.popleft()
        if cur == target:
            idx = cur
            while idx != start:
                path.append(idx)
                idx = visited[idx]
            path.append(start)
            return cur_time
    
        if cur+1 < 100001 and visited[cur+1] == -1:
            que.append((cur+1, cur_time+1))
            visited[cur+1] = cur
        
        if cur-1 >= 0 and visited[cur-1] == -1:
            que.append((cur-1, cur_time+1))
            visited[cur-1] = cur
        
        if cur*2 < 100001 and visited[cur*2] == -1:
            que.append((cur*2, cur_time+1))
            visited[cur*2] = cur

visited = [-1] * 100001
path = []

N, K = map(int, input().split())

print(bfs(N, K))
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(*path[::-1])