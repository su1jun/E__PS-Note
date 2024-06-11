from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([i for i in range(1, n+1)])
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
#    print(f"q : {q}")
print(q[0])
