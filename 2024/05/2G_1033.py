import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
visited = [False] * N
mass = [0] * N

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a % b)

cm = 1
for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    cm *= ((p*q) // gcd(p, q))
mass[0] = cm

def dfs(node):
    visited[node] = True
    for next_node, np, nq in graph[node]:
        if not visited[next_node]:
            mass[next_node] = mass[node] * nq // np
            dfs(next_node)

dfs(0)
cd = mass[0]
for i in range(1, N):
    cd = gcd(cd, mass[i])

for i in range(N):
    mass[i] //= cd
print(*mass)
