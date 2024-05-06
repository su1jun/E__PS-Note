import sys
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
visited = [0] * (V+1)
graph = [[0] * V+1 for _ in range(V+1)]

for _ in range(V):
    a, b, c = map(int, input().split())
    graph[a][b] = c

answer = INF

def dfs(node):
    global answer
    if node == V:
        answer = min(answer, sum(visited))
        return
    for i in range(1, V+1):
        if graph[node][i] and not visited[i]:
            visited[i] = 1
            dfs(i)
            visited[i] = 0

parent = [i for i in range(V+1)]

def find(x):
    if parent[x] == x: return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b: parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return find(a) == find(b)