<<<<<<< HEAD
# ACM Craft
from collections import deque
import sys
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        N, K = map(int,input().split())
        cost = [0] + list(map(int, input().split()))
        link = [[] for _ in range(N+1)]
        cntLink = [-1] + [0] * N
        for _ in range(K):
            a, b = map(int,input().split())
            link[a].append(b)
            cntLink[b] += 1
        end = int(input())

        # 시작 정점들 넣기
        dp = [0] * (N+1)
        q = deque()
        for i in range(1, N+1):
            if cntLink[i] == 0:
                q.append(i)
                dp[i] = cost[i]
                
        # 위상 정렬
        while q:
            curNode = q.popleft()
            for toNode in link[curNode]:
                cntLink[toNode] -= 1
                dp[toNode] = max(dp[toNode], dp[curNode]+cost[toNode])
                if cntLink[toNode] == 0:
                    q.append(toNode)
            
            # 목표 지점의 값을 구했음
            if cntLink[end] == 0:
                print(dp[end])
                break
=======
# ACM Craft
from collections import deque
import sys
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        N, K = map(int,input().split())
        cost = [0] + list(map(int, input().split()))
        link = [[] for _ in range(N+1)]
        cntLink = [-1] + [0] * N
        for _ in range(K):
            a, b = map(int,input().split())
            link[a].append(b)
            cntLink[b] += 1
        end = int(input())

        # 시작 정점들 넣기
        dp = [0] * (N+1)
        q = deque()
        for i in range(1, N+1):
            if cntLink[i] == 0:
                q.append(i)
                dp[i] = cost[i]
                
        # 위상 정렬
        while q:
            curNode = q.popleft()
            for toNode in link[curNode]:
                cntLink[toNode] -= 1
                dp[toNode] = max(dp[toNode], dp[curNode]+cost[toNode])
                if cntLink[toNode] == 0:
                    q.append(toNode)
            
            # 목표 지점의 값을 구했음
            if cntLink[end] == 0:
                print(dp[end])
                break
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
solve()