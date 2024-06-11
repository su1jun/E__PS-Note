import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 추의 갯수
arr = sorted(list(map(int, input().split()))) # 추의 무게 수

top = arr[0] # 최고값
if top != 1:
    print(1)
else:
    ans = 0 # 답

    for i in range(1, N):
        if top + 1 >= arr[i]:
            top += arr[i]
        else:
            break

    print(top+1)