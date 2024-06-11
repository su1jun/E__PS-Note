# 숫자의 대소 and 인덱스의 대소로 순서 파악
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i, x in enumerate(arr):
    dp[x] = i+1
top = -1
cnt = 1
for i in range(1, N):
    if dp[i] < dp[i+1]:
        cnt += 1
        # if 문으로 처리하는게 더 빠른듯
        top = max(top, cnt)
    else:
        cnt = 1
print(N - top)