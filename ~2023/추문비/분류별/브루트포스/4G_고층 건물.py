import sys
input = sys.stdin.readline
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
 
N = int(input())
 
buil = list(map(int, input().split()))
 
res = 0
for i1, y1 in enumerate(buil):
    x1 = i1 + 1
    c_s_right = None
    v_right = 0
    for i2 in range(i1+1, N):
        x2 = i2 + 1
        y2 = buil[i2]
        s_right = slope(x1, y1, x2, y2)
        if c_s_right is None or c_s_right < s_right:
            c_s_right = s_right
            v_right += 1

    c_s_left = None
    v_left = 0
    for i3 in range(i1-1, 0, -1):
        x2 = i3 + 1
        y2 = buil[i3]
        s_left = slope(x1, y1, x2, y2)
        if c_s_left is None or c_s_left > s_left:
            c_s_left = s_left
            v_left += 1
 
    if (v_left + v_right) > res: res = v_left + v_right

print(res)