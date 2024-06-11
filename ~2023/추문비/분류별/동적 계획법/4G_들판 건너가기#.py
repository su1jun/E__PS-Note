import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
tmp = [arr[0]]
ans = 0
for i in range(2, N):
    if arr[i-2] < arr[i-1] and arr[i-1] > arr[i]:
        tmp.append(arr[i-1])
    elif arr[i-2] > arr[i-1] and arr[i-1] < arr[i]:
        tmp.append(arr[i-1])
tmp.append(arr[-1])

for i in range(1, len(tmp)):
    ans += (tmp[i]-tmp[i-1])**2
print(ans)