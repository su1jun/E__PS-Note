import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    nums = dict()
    for _ in range(N):
        A, B = map(str, sys.stdin.readline().split())
        if B in nums:
            nums[B] += 1
        else:
            nums[B] = 2
    nums2 = list(nums.values())
    anw = 1
    for i in nums2:
        anw *= i
    print(anw-1)

