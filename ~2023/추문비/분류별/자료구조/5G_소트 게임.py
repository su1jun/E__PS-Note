import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst):
    que = deque(lst)
    parr, n = que[0]
    Visited.add(parr)
    while que:
        parr, n = que.popleft()
        if parr == ans:
            return n
        parr = "v" + parr
        l = len(parr)
        for i in range(K, l):
            tmp = parr[1:i-K+1] + parr[i:i-K:-1] + parr[i+1:]
            if tmp not in Visited:
                Visited.add(tmp)
                que.append((tmp, n+1))
    else:
        return -1

N, K = map(int, input().split())
arr = input().split()

string = "".join(arr)
ans = "".join(sorted(arr))

Visited = set()
print(bfs([(string, 0)]))