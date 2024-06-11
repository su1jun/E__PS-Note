import sys
input = sys.stdin.readline

# 입력값
N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

# 설치 거리 기준
bot = 0 # 최소거리
top = (arr[-1] - arr[0]) # 최대거리
print(f"top : {top}, bot : {bot}")

while bot <= top:
    mid = (bot + top)//2 # 중간값
    print(f"mid : {mid}")
    cnt = 1 # 설치한 공유기
    tmp = arr[0] # 마지막 설치 장소

    for i in range(1, N):
        if arr[i] - tmp >= mid:
            tmp = arr[i]
            cnt += 1
    print(f"/cnt : {cnt}")

    if cnt < C: # 설치 갯수가 적을때
        top = mid-1
        print(f"top : {top}")
    else: # 설치 갯수가 많을때
        bot = mid+1
        print(f"bot : {bot}")

print(top)