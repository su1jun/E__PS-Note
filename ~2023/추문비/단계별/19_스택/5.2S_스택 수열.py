import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

count = 1
stk = []
ans = []

for _ in range(n):
    data = int(input())

    while count <= data:
        stk.append(count)
        ans.append('+')
        count += 1

    if stk.pop() == data:
        ans.append('-')

    else:
        print("NO")
        exit(0)

print("\n".join(ans))