#$ 일정부분 합이 K일 조건 $#
import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split()) # N : 수열 길이, K : 목표 합
arr = list(map(int, input().split())) # 수열
data = defaultdict(int)
ans = 0
psum = [0] * (N+1)
for i in range(1, N+1):
    psum[i] += arr[i-1] + psum[i-1]
    if psum[i] == K:
        ans += 1
        
    ans += data[psum[i]-K]
    data[psum[i]] += 1

print(ans)