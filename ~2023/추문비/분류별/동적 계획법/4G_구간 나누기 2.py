# 이분탐색, 구간의 최대-최소 값을 mid로
import sys
input = sys.stdin.readline

def chkterm(midValue):
    low = arr[0]
    high = arr[0]
    k = 1

    for i in arr:
        if high < i: # high 값
            high = i

        if low > i: # low 값
            low = i
        
        if high - low > midValue: # 구간 확정
            k += 1
            low = i
            high = i

    return k <= M # 조건 만족

N, M = map(int, input().split())
arr = list(map(int, input().split()))

top = max(arr)
bot = 0
ans = top

while bot <= top:
    mid = (bot + top) // 2 # 찾는 값

    if chkterm(mid):
        top = mid - 1
        ans = min(ans, mid) # 최소값으로
    else:
        bot = mid + 1

print(ans)