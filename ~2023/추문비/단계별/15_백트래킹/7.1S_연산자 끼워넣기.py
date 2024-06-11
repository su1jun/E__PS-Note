import sys
import math
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
oprs = list(map(int, input().split()))

data = []

def f(lst, lst2):
  if sum(lst) == 0:
    # print("완성")
    ans = nums[0]
    for i in range(N-1):
        if lst2[i] == 0:
            ans += nums[i+1]
        elif lst2[i] == 1:
            ans -= nums[i+1]
        elif lst2[i] == 2:
            ans *= nums[i+1]
        else:
            ans /= nums[i+1]
            if ans < 0:
                ans = math.ceil(ans)
            else:
                ans = math.floor(ans)
    data.append(ans)
    return

  for i in range(4):
    if lst[i] == 0:
      continue
    idx = lst.copy()
    idx[i] -= 1
    # print(f"{i} 번째 실행 / lst : {lst}, lst2 : {lst2 + [i]}")
    f(idx, lst2 + [i])

f(oprs, [])
# print(f"data : {data}")
print(max(data))
print(min(data))
 


