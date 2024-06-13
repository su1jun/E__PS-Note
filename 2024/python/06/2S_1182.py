import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sum):
    global cnt
    if idx >= N:
        if sum == S: cnt += 1
        return

    subset_sum(idx + 1, sum + arr[idx])
    subset_sum(idx + 1, sum)

subset_sum(0, 0)
print(cnt - (1 if S == 0 else 0))