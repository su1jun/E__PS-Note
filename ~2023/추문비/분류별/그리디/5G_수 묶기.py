import sys
input = sys.stdin.readline

N = int(input())
arr = []
ans = 0
idx = 0
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

if N % 2 == 0: # 짝수 리스트 처리
    for i in range(0, N, 2):
        a = arr[i]*arr[i+1]
        if a > arr[i]:
            ans += arr[i]*arr[i+1]
        else:
            ans += max(a, arr[i]+arr[i+1])

else: # 홀수 리스트 처리
    for i in range(0, N-1, 2):
        if arr[i] > 0: # i는 양수
            a = arr[i]*arr[i+1]

            if a > arr[i]: # 일반적일때
                ans += a
            else:
                ans += arr[i]
                if arr[i+1] > 0: # n > 1로 나온 경우
                    ans += arr[i+1] 

                else: # n > 0 or 음수로 나온 경우
                    # += 처리 후 이후 짝수 배열 계산
                    idx = i
                    break

        else: # i부터 음수
            # += 처리 후 이후 짝수 배열 계산
            ans += arr[i]
            idx = i+1
            break

    else: # 음수 or 0 발견이 안됐을때
        ans += arr[-1]

    if idx: # 남은 짝수 배열 계산
        for i in range(N-1, idx, -2):
            a = arr[i-1]*arr[i]
            ans += a

print(ans)