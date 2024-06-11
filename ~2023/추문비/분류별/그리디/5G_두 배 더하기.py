import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 배열 크기
arr = sorted(list(map(int, input().split())), reverse=True)
cnt = 0 # 연산 횟수

while arr[0]:
    for i in range(N):
        if arr[i] % 2 == 1:
            arr[i] -= 1
            cnt += 1
    if arr[0] == 0:
        break

    for i in range(N):
        arr[i] //= 2
    cnt += 1
print(cnt)