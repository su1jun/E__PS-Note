import sys
import heapq
input = sys.stdin.readline

# 초기값
N = int(input())
heapL = [] # 최대힙
heapR = [] # 최소힙

# 첫번째
mid = int(input())
print(mid)

# 두번째
x = int(input())
if mid <= x:
    print(mid)
    heapq.heappush(heapL, (-mid, mid))
    heapq.heappush(heapR, x)
else:
    print(x)
    heapq.heappush(heapL, (-x, x))
    heapq.heappush(heapR, mid)
    mid = x

#print(f"mid : {mid} // heapL : {heapL} // heapR : {heapR}")

# 세번째 부터는
for _ in range(2, N):
    x = int(input())
    lenL = len(heapL)
    lenR = len(heapR)
    
    if mid <= x: # 우측에 입력값 삽입
        heapq.heappush(heapR, x)
        lenR += 1

        while lenL < lenR: # 우측이 더 많은 숫자가 있을때

            tmp = heapq.heappop(heapR)
            heapq.heappush(heapL, (-tmp, tmp))
            lenL += 1
            lenR -= 1

        mid = heapL[0][1]
        print(mid)

    else: # 좌측에 입력값 삽입
        heapq.heappush(heapL, (-x, x))
        lenL += 1
        
        # if x == -99:
        #     print(f"%lenL : {lenL} %lenR : {lenR}")
        #     print(f"mid : {mid} // heapL : {heapL} // heapR : {heapR}")

        while lenL > lenR + 1: # 좌측이 더 많은 숫자가 있을때
            tmp = heapq.heappop(heapL)[1]
            heapq.heappush(heapR, tmp)
            lenL -= 1
            lenR += 1
        mid = heapL[0][1]
        print(mid)

    

