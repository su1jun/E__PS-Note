import sys
input = sys.stdin.readline
 
# 초기 입력
N = int(input()) # N : 수열의 크기
stack = [[int(input()), 1]]  # stack : 사람 배열
ans = 0

for _ in range(1, N):
    t = 1 # 같은 키의 사람 처리
    K = int(input()) # 현 위치 사람의 키
    while stack and stack[-1][0] <= K:
        if stack[-1][0] == K:
            t = stack[-1][1] + 1
        ans += stack.pop()[1]

    else:
        if stack:
            ans += 1

        stack.append([K, t])
    print(f"스택 : {stack}")
print(ans)