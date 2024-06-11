import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
ans = 999999
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for chi in combinations(chicken, M):
    tmp = 0
    for h in home: 
        c_len = 999
        for j in range(M):
            c_len = min(c_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        tmp += c_len
    ans = min(ans, tmp)

print(ans)