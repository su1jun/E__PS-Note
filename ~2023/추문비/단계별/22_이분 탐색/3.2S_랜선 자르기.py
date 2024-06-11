import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lens = []

for _ in range(K):
    lens.append(int(input()))

top = max(lens)
bot = 1
mid = (top+bot) // 2
while bot <= top:
    mid = (top+bot) // 2
    cnt = 0
    print(f"mid : {mid}")
    for i in lens:
        cnt += i // mid
    if cnt >= N:
        bot = mid+1
        print(f"bot : {bot}")
    else:
        top = mid-1
        print(f"top : {top}")
print(top)
