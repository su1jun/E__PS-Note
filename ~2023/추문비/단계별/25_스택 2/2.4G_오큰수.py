import sys
input = sys.stdin.readline
 
# 초기 입력
N = int(input()) # N : 수열의 크기
A = list(map(int, input().split())) # A : 수열

ans = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)