import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    global team_no

    visited[n] = True
    team.append(n)

    if visited[arr[n]] == True:
        if arr[n] in team:
            team_no -= len(team[team.index(arr[n]):])
        return

    else:
        dfs(arr[n])

T = int(input())

for _ in range(T):
    N = int(input())

    arr = [0]
    arr.extend([int(x) for x in input().rstrip().split()])

    visited = [False] * (N + 1)
    team_no = N
    for i in range(1, N + 1):
        if not visited[i]:
            team = []
            dfs(i)

    print(team_no)