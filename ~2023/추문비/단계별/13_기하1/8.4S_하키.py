import sys
W, H, X, Y, P = map(int, sys.stdin.readline().split())
cnt = 0

for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())
    if x < X:
        cnt += ((x-X)**2 + (y-Y-H//2)**2 <= (H//2)**2)
    elif X <= x and x <= X + W:
        cnt += (Y <= y and y <= Y + H)
    else:
        cnt += ((x-X-W)**2 + (y-Y-H//2)**2 <= (H//2)**2)
    
print(cnt)

