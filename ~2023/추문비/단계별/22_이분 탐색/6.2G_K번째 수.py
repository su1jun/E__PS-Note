import sys
input = sys.stdin.readline

# 입력값
N = int(input())
K = int(input())

bot = 1 # 최소값
top = N*N # 최대값
print(f"top : {top}, bot : {bot}")

while bot <= top:
    mid = (bot + top)//2 # 중간값
    print(f"mid : {mid}")

    cnt = 0 # 숫자 갯수
    for i in range(1, N+1):
        cnt += min(mid//i, N) 
    print(f"/cnt : {cnt}")

    if cnt >= K: # 찾은 값이 많을때 (ans > k)
        top = mid-1
        print(f"top : {top}")
    else: # 찾은 값이 많을때 (ans < k)
        bot = mid+1
        print(f"bot : {bot}")

print(top+1)