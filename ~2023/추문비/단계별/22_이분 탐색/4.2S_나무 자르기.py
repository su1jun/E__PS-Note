import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lens = list(map(int, input().split()))

top = max(lens)
bot = 0
mid = (top+bot) // 2
while bot <= top:
    mid = (top+bot) // 2
    cnt = 0
    print(f"mid : {mid}")
    for i in lens:
        if i > mid:
            cnt += i-mid
    print(f"/cnt : {cnt}")
    if cnt >= M:
        bot = mid+1
        print(f"bot : {bot}")
    else:
        top = mid-1
        print(f"top : {top}")
print(top)