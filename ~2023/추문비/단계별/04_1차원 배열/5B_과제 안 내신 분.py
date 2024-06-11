import sys
input = sys.stdin.readline

arr1 = set([i for i in range(1, 31)])
arr2 = set([int(input()) for _ in range(28)])

for i in sorted(list(arr1 - arr2)):
    print(i)