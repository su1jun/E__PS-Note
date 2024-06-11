import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
ans = 0
for i in range(n):
    ans += a[i] * b[i]
print(ans)
