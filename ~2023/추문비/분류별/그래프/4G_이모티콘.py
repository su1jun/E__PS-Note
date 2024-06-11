import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
que = deque()
que.append((1, 0))
visited = dict()
visited[(1, 0)] = 0

while que:
    s, c = que.popleft()
    if s == N:
        print(visited[(s, c)])
        break
        
    # 1번 연산 : 화면에 있는 모든 이모티콘을 복사
    if (s, s) not in visited.keys():
        visited[(s, s)] = visited[(s, c)] + 1
        que.append((s, s))
    # 2번 : 화면에 있는 모든 이모티콘 중 1개 삭제
    if (s-1, c) not in visited.keys():
        visited[(s-1, c)] = visited[(s, c)] + 1
        que.append((s-1, c))
    # 3번 연산 : 클립보드에 있는 이모티콘을 붙여넣기
    if (s+c, c) not in visited.keys():
        visited[(s+c, c)] = visited[(s, c)] + 1
        que.append((s+c, c))