import sys
import math

N = int(sys.stdin.readline())

nums = [int(sys.stdin.readline())]

if N > 2:
    for _ in range(N-1):
        nums.append(int(sys.stdin.readline()))
        if _ == 1:
            GCD = math.gcd(abs(nums[-1] - nums[-2]), abs(nums[-2] - nums[-3]))
        elif _ > 1:
            GCD = math.gcd(abs(nums[-1] - nums[-2]), GCD)

else:
    for _ in range(1):
        nums.append(int(sys.stdin.readline()))
        GCD = abs(nums[-1] - nums[-2])


cnt = 2
cd = [GCD]
while cnt <= math.sqrt(GCD):
    if GCD % cnt == 0:
        cd.append(cnt)
        if cnt != GCD // cnt:
            cd.append(GCD // cnt)
    cnt += 1
cd.sort()
for i in cd:
    print(i, end=' ')


# from math import gcd
# N = int(input())
# A = sorted([int(input()) for i in range(N)])
# B = sorted([A[i+1]-A[i] for i in range(N-1)])
# d = B[0]
# for i in range(1, N-1):
#     d = gcd(d, B[i])
    
# C = []
# for i in range(2, int(d**0.5) + 1):
#     if d % i == 0:
#         C.append(i)
#         C.append(d//i)
# C.append(d)
# print(*sorted(list(set(C))))