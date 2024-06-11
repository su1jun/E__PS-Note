import sys
input = sys.stdin.readline

def f(num, n):
    lst = []
    for i in num:
        # print(f"f(i) : {lst[i]}")
        lst.append(i + " + " + str(n))
        lst.append(str(n) + " + " + i)
    return lst

T = int(input())
dp = [0] * 11
dp[0] = ["1"]

for i in range(1, 3):
    dp[i] = list(set(f(dp[i-1], 1)))
    dp[i].append(str(i+1))
    # print(f"i : {i} // cnt : {len(dp[i])}")
    # print(f"{dp[i]}")
for i in range(3, 11):
    dp[i] = list(set(f(dp[i-1], 1) + f(dp[i-2], 2) + f(dp[i-3], 3)))
    # print(f"i : {i} // cnt : {len(dp[i])}")
    # print(f"{dp[i]}")
# print(dp)
for _ in range(T):
    print(len(dp[int(input())-1]))