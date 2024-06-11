import sys
import math
import itertools
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    N = int(input())
    coords = []
    
    x_total = 0
    y_total = 0
    for _ in range(N):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        coords.append([x, y])
    
    res = math.inf
    com = list(itertools.combinations(coords, int(N/2)))
    com_half = int(len(com) / 2)
    for sum_coord in com[:com_half]:
        sum_coord = list(sum_coord)
 
        x1_total = 0
        y1_total = 0
        for x1, y1 in sum_coord:
            x1_total += x1
            y1_total += y1
        
        x2_total = x_total - x1_total
        y2_total = y_total - y1_total
        
        res = min(res, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))
 
    ans.append(res)
 
for result in ans:
    sys.stdout.write(str(result)+'\n')