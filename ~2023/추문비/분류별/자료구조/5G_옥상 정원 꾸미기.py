import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input())]
cnt = 0
for _ in range(N-1):
    tmp = int(input())
    while arr and arr[-1] <= tmp:
        arr.pop()
    cnt += len(arr)
    arr.append(tmp)
print(cnt)