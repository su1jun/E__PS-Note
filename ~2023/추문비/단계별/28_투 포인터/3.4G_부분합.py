import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = sys.maxsize

while True:
    if sum >= S:
        min_length = min(min_length, right - left)
        sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum += arr[right]
        right += 1

if min_length == sys.maxsize: min_length = 0
print(min_length)