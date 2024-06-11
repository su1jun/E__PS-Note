import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    n = int(input())
    if n == 0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))