import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
que = deque()

while True:
    k = int(input())
    if k == -1:
        break
    if k:
        if len(que) <= N:
            que.append(k)
    else:
        que.popleft()

if que:
    print(*que)
else:
    print("empty")
