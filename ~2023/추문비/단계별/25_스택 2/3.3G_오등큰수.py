import sys
from collections import Counter
input = sys.stdin.readline
 
# 초기 입력
N = int(input()) # N : 수열의 크기
A = list(map(int, input().split())) # A : 수열
cnt = Counter(A)

ans = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)