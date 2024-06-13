import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, i):
        if arr[i] < arr[j] + arr[i-j]:
            arr[i] = arr[j] + arr[i-j]

print(arr[N])