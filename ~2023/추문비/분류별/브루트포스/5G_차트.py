import sys
import itertools
input = sys.stdin.readline

def ckh(arr):
    prefix = [0] * (N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    prefix_s = set(prefix)
    cnt = 0
    for i in prefix:
        if i < 50:
            if (i+50) in prefix_s:
                cnt += 1
    return cnt

N = int(input()) # 갯수
arr = list(map(int, input().split())) # %
if max(arr) > 50:
    print(0)
else:
    brt = list(itertools.permutations(arr, N))
    ans = 0
    for i in brt:
        tmp = ckh(i)
        if ans < tmp:
            ans = tmp
    print(ans)