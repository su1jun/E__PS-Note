import sys
import math
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
nums = []

if N == 1:
    print(arr[0])
else:
    for i in range(N-1):
        nums.append(arr[i+1] - arr[i])

    ans = math.gcd(nums[0], nums[1])
    if N > 2:
        for i in range(2, len(nums)):
            ans = math.gcd(ans, nums[i])
    print(ans)