import sys
input = sys.stdin.readline

#초기 입력
H, W = map(int, input().split()) # H X W(가로)
arr = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    left = max(arr[:i])
    right = max(arr[i+1:])

    tmp = min(left, right)

    if arr[i] < tmp:
        ans += tmp - arr[i]

print(ans)