import sys
input = sys.stdin.readline

def cmb1(lst, n):
    dp = []
    sum = 0
    if n == 1:
        return lst

    for i in range(1, n):
        sum += lst[i-1]
        if lst[i]*sum < 0:
            dp.append(sum)
            sum = 0
        if i == n-1:
            dp.append(sum+lst[i])
    return dp

def cmb2_L(lst):
    dp = []
    len_lst = len(lst)
    if len_lst != 0:
        if len_lst % 2 == 0:
            for i in range(0, len_lst, 2):
                dp.append(lst[i] + lst[i+1])
        else:
            dp.append(lst[0])
            for i in range(1, len_lst, 2):
                dp.append(lst[i] + lst[i+1])
    return dp

def cmb2_R(lst):
    dp = []
    len_lst = len(lst)
    if len_lst != 0:
        if len_lst % 2 == 0:
            for i in range(0, len_lst, 2):
                dp.append(lst[i] + lst[i+1])
        else:
            for i in range(0, len_lst-1, 2):
                dp.append(lst[i] + lst[i+1])
            dp.append(lst[-1])
    return dp

n = int(input())
nums = list(map(int, input().split()))
dp = cmb1(nums, n)

while True:
    m = max(dp)
    a = dp.index(m)

    if len(dp) == 1 and dp[0] < 0:
        m = max(nums)

    if len(dp) <= 3:
        break

    left = dp[0:a]
    if a == len(dp) - 1:
        right = []
    else:
        right = dp[a+1:]

    dp_left = cmb2_L(left)
    dp_right = cmb2_R(right)

    dp = cmb1(dp_left + [m] + dp_right, len(dp_left) + 1 + len(dp_right))

print(m)

####

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
  data[i] = max(data[i], data[i] + data[i-1])
  
print(max(data))