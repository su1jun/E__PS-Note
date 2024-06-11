import sys
input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, visited, total):
    global ans
    if len(visited) == N+1:
        ans += total
        return
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            dfs(nr, nc, visited, total*p[idx])
            visited.pop()

N, ep, wp, sp, np = map(int, input().split())
p = [ep, wp, sp, np]
ans = 0

dfs(0, 0, [(0, 0)], 1)
print(ans * (0.01 ** N))
