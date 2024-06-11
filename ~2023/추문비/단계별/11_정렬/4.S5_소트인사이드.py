import sys

while True:
    Nums = []
    N = sys.stdin.readline()
    for i in N[0:-1]:
        Nums.append(int(i))

    Nums.sort(reverse=True)

    for i in Nums:
        print(i, end="")
    print()

# 다른 정답
# import sys
# n = sys.stdin.readline().rstrip()
# print("".join(sorted(n, reverse=True)))