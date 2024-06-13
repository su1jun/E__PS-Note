import sys
input = sys.stdin.readline

N = int(input())
reqest = list(map(int, input().split()))
budget = int(input())

left = 0
right = max(reqest)
ans = 0

while left <= right:
    mid = (left + right) // 2
    total = 0

    for req in reqest:
        total += min(req, mid)

    if total <= budget:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)