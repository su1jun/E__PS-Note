import sys

n, m = map(int, sys.stdin.readline().split())

def f(nums):
  if len(nums) == m:
    print(' '.join(map(str, nums)))
    return

  for i in range(1, n + 1):
    f(nums + [i])

f([])