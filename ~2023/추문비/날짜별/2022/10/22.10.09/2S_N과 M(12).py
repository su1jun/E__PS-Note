import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
temp = []

def f():
    if len(temp) == m:
        print(*temp)
        return
    memo = 0
    for i in range(n):
        if temp:
            if temp[-1] <= arr[i]:
                if memo != arr[i]:
                    temp.append(arr[i])
                    memo = arr[i]
                    f()
                    temp.pop()
        else:
            if memo != arr[i]:
                temp.append(arr[i])
                memo = arr[i]
                f()
                temp.pop()

f()