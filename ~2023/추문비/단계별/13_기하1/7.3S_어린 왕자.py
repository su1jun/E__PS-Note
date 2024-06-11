import sys
T = int(sys.stdin.readline())

def out(x, y, cx, cy, r):
    if (x - cx)**2 + (y - cy)**2 > r**2:
        return True
    else:
        return False

for _ in range(T):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if out(x1, y1, cx, cy, r):
            if out(x2, y2, cx, cy, r):
                ans += 1
        else:
            if not(out(x2, y2, cx, cy, r)):
                ans += 1
    print(n-ans)
