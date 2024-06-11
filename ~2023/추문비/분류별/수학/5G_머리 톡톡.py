import sys
from collections import defaultdict
input = sys.stdin.readline

def f(n): # 약수 구하기
    dvs = set()
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            dvs.add(i)
            dvs.add(n // i)
    #print(n, dvs)
    return dvs

N = int(input()) # 갯수
arr = []
nums = defaultdict(int)
for _ in range(N):
    K = int(input())
    arr.append(K)
    nums[K] += 1

for i in arr:
    ans = 0
    for j in f(i):
        ans += nums[j]
    print(ans-1)
