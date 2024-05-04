import sys

input = sys.stdin.readline
r, c = list(map(int, input().split()))
graph = [[0] * c for _ in range(r)]

for i in range(r):
    temp = input().strip()
    for j in range(c):
        graph[i][j] = temp[j]

visited = [0] * 26
visited[ord(graph[0][0]) - 65] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth):
    global result
    result = max(result, depth)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            temp = ord(graph[nx][ny]) - 65
            if visited[temp] == 0:
                visited[temp] = 1
                dfs(nx, ny, depth + 1)
                visited[temp] = 0

global result
result = 0
dfs(0, 0, 1)
print(result)