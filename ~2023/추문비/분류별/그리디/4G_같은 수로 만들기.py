# 극소에서 더해가기
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = [int(input())]
max_num = stack[-1]

for _ in range(n - 1):
    k = int(input())
    if stack[-1] < k:
        cnt += k - stack.pop()
        max_num = max(max_num, k)
    stack = [k]

cnt += max_num - sum(stack)
print(cnt)