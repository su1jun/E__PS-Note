import sys
from collections import deque
input = sys.stdin.readline

def solution(m, n, puddles):
    graph = [[0] * (n+1) for _ in range(m+1)]
    graph[1][1] = 1
    que = deque([[1, 1]])

    while que:
        x, y = que.popleft()
        nx = x + 1
        ny = y + 1
        if x < m and not graph[nx][y] and not [nx, y] in puddles:
            graph[nx][y] = (graph[x][y] + graph[nx][y-1]) % 1000000007
            que.append([nx, y])
        if y < n and not graph[x][ny] and not [x, ny] in puddles:
            graph[x][ny] = (graph[x][y] + graph[x-1][ny]) % 1000000007
            que.append([x, ny])

    for i in graph:
        print(*i)
    return max(0, graph[m][n]) % 1000000007

print(solution(6, 6, [[4, 3], [1, 2], [2, 4], [5, 1], [1, 6]]))
print(solution(3, 3, [[2, 1], [1, 2]]))