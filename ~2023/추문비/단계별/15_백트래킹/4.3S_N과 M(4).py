import sys

n, m = map(int, sys.stdin.readline().split())

def f(nums):
  if len(nums) == m:
    print(' '.join(map(str, nums)))
    return

  for i in range(1, n + 1):
        if len(nums) == 0:
            f(nums + [i])
        else:
            if nums[-1] <= i:
                f(nums + [i])

f([])