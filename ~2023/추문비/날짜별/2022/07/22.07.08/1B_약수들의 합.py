import sys

n = int(sys.stdin.readline())
while n != -1:
    lst = []
    for i in range(1, int(n**(1/2))+1):
        if i == 1:
            lst.append(i)
        elif n % i == 0:
            lst.append(i)
            lst.append(n // i)
    if sum(lst) == n:
        print(f"{n} =", end="")
        for i in sorted(lst):
            if i == 1:
                print("", i, end="")
            else:
                print(" +", i, end="")
        print()
    else:
        print(n, "is NOT perfect")
    n = int(sys.stdin.readline())
