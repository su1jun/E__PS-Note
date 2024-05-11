import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque(enumerate(map(int, input().split())))
ans = []

while Q:
    idx, paper = Q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        Q.rotate(-(paper - 1))
    elif paper < 0:
        Q.rotate(-paper)

print(*ans)
