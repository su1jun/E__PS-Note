import sys
import math

N = int(sys.stdin.readline())
nums = list(map(int, (sys.stdin.readline().split())))

std = nums[0]
for i in range(1, N):
    GCD = math.gcd(std, nums[i])
    print(f"{std//GCD}/{nums[i]//GCD}")