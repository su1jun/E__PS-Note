import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = []

start = arr[0]
max_pow = 0

for i, x in enumerate(arr):
    temp = x
    pow = 0
    while temp % 3 == 0:
        temp //= 3
        pow += 1
    if (pow > max_pow) or (pow == max_pow and x < start):
        max_pow = pow
        start = x

ans.append(start)

for i in range(N):
    if ans[-1] * 2 in arr:
        ans.append(ans[-1] * 2)
        continue
    if ans[-1] % 3 == 0 and ans[-1] // 3 in arr:
        ans.append(ans[-1] // 3)
        continue
    break

if len(ans) == N:
    print(*ans)