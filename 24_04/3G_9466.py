import sys
input = sys.stdin.readline

T = int(input())

def dfs(i):
    global team_no

    visited[i] = True
    team.append(i)
    select = selected[i]

    if visited[select]:
        if select in team:
            team_no += len(team[team.index(select):])
    else:
        dfs(select)

for _ in range(T):
    N = int(input())
    selected = [0] + list(map(int, input().split()))

    visited = [False] * (N+1)
    team_no = 0

    for i in range(1, N+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(N - team_no)