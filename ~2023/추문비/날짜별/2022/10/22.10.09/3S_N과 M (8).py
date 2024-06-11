import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def f(nums):
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return

    for i in data:
        if nums:
            if i >= nums[-1]:
                f(nums + [i])
        else:
            f(nums + [i])

f([])