import sys
input = sys.stdin.readline

# 입력값
n = int(input())
arr = list(map(int, input().split()))
lst = [0]

for i in arr:
    if lst[-1] < i: # 가장 큰 수를 만나면
        lst.append(i)
    else: # 그렇지 않으면 숫자 넣기
        bot = 0
        top = len(lst)

        while bot < top: # 이분탐색
            mid = (top+bot)//2
            if lst[mid] < i:
                bot = mid+1
            else:
                top = mid
        lst[top] = i
    print(f"lst {lst}")
print(len(lst)-1)