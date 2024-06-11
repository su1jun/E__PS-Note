# bfs 방문여부
import sys
from collections import deque
input = sys.stdin.readline

step = [i for i in range(1, 7)]
def bfs(x):
    que = deque([x])
    while que or not visited[100]:
        px = que.popleft()

        if graph[px]: # 사다리나 뱀의 출발지 일때
            nx = graph[px]
            if not visited[nx]:
                order[nx] = order[px] + 1
                if not graph[nx]: # 도착칸이 다른 출발지가 아닐때
                    visited[nx] = 1
                que.append(nx)

        else: # 사다리나 뱀의 출발지가 아닐때 = 주사위를 굴릴때
            for i in step:
                nx = px + i
                if 0 < nx <= 100:
                    if graph[nx]:
                        nx = graph[nx]
                    if not visited[nx]:
                        order[nx] = order[px] + 1
                        if not graph[nx]: # 도착칸이 다른 출발지가 아닐때
                            visited[nx] = 1
                        visited[nx] = 1
                        que.append(nx)
    else:
        return order[100]

N, M = map(int, input().split())
graph = [0] * 101
visited = [0] * 101
order =  [0] * 101

for _ in range(N+M):
    a, b = map(int, input().split())
    graph[a] = b

print(bfs(1))