import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == "push_front":
        stack.insert(0, int(a[1]))
    elif a[0] == "push_back":
        stack.append(int(a[1]))
    elif a[0] == "pop_front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
            del stack[0]
    elif a[0] == "pop_back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])