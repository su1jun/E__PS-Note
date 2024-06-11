import sys
n = int(sys.stdin.readline())
s = 0
while s*(s+1)//2 < n:
    s += 1
s -= 1
if n - s*(s+1)//2 <= s:
    print(s)
else:
    print(s + 1)