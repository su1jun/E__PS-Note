import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        a, b=map(int, input().split())
        parent[b] = a

    ta, tb = map(int,input().split())
    tracking_ta = []
    while True:
        if ta == 0:
            break
        tracking_ta.append(ta)
        ta = parent[ta]
        
    while True:
        if tb in tracking_ta:
            print(tb)
            break
        tb = parent[tb]