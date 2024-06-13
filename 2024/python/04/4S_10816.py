import sys, collections

input = sys.stdin.readline
N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))

counter = collections.Counter(num1)
for i in num2:
    if i in counter:
        print(counter[i], end=' ')
    else:
        print(0, end=' ')