from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
od = list(map(int, input().split()))

rtq = deque([i for i in range(1, N+1)])
cnt = 0

for i in od:
#    print(f"{i} 서칭")
    if i == rtq[0]:
        rtq.popleft()
#        print(f"연산완료 : {rtq}")
    else:
        l = len(rtq)
        idx = rtq.index(i)
        if idx <= (l // 2):
            for _ in range(idx):
                rtq.append(rtq.popleft())
#                print(f"{_}회 왼 > 오 : {rtq}")
                cnt += 1
            rtq.popleft()
#            print(f"연산완료 : {rtq} / 카운트 : {cnt}")
        else:
            for _ in range(l-idx):
                rtq.appendleft(rtq.pop())
#                print(f"{_}회 오 > 왼 : {rtq}")
                cnt += 1
            rtq.popleft()
#            print(f"연산완료 : {rtq} / 카운트 : {cnt}")
print(cnt)
