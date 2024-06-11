<<<<<<< HEAD
import sys
input = sys.stdin.readline

N = int(input())
d = [1, 0, 1, 0, 3, 0, 15, 0, 105, 0]
nums = [0] * 10
res = 1

for _ in range(N):
    temp = int(input())
    nums[temp // 10] += 1
    nums[temp % 10] += 1
for i in range(10):
    res *= d[nums[i]]
=======
import sys
input = sys.stdin.readline

N = int(input())
d = [1, 0, 1, 0, 3, 0, 15, 0, 105, 0]
nums = [0] * 10
res = 1

for _ in range(N):
    temp = int(input())
    nums[temp // 10] += 1
    nums[temp % 10] += 1
for i in range(10):
    res *= d[nums[i]]
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(res)