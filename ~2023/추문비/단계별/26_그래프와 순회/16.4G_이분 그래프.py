import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

def bfs(start, group):
    queue = deque([start])
    visited[start] = group
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')