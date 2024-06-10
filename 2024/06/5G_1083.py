import sys
input = sys.stdin.readline

N = int(input())
Arr = list(map(int, input().split()))
S = int(input())

for i in range(N):
    for j in range(i, min(N, i+S+1)):
        mx = Arr[i]
        idx = i
        if Arr[j] > mx:
            mx = Arr[j]
            idx = j
    
    for j in range(idx, i, -1):
        Arr[j], Arr[j-1] = Arr[j-1], Arr[j]

    S -= (idx - i)
    if S <= 0: break
print(*Arr)

# n, nums = int(input()), list(map(int, input().split()))
# s = int(input())

# for i in range(n):
#     # 탐색
#     max_num = max(nums[i: min(n, i + s + 1)])
#     idx = nums.index(max_num)
#     # 교환
#     for j in range(idx, i, -1):
#         nums[j], nums[j - 1] = nums[j - 1], nums[j]
#     # 후처리
#     s -= (idx - i)
#     if s <= 0: break

# print(*nums)