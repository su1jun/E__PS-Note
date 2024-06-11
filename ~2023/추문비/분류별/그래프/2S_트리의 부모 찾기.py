# bfs로 방문처리
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

q = deque([1]) # root
parent = [""] * (N+1)

while q:
    tmp = q.popleft()
    for i in tree[tmp]:
        if parent[i] == "" and i != 1:
            parent[i] = str(tmp)
            q.append(i)
print("\n".join(parent[2:]))