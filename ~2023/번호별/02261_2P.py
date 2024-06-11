<<<<<<< HEAD
import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()

def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2

def dac(start, end):
    if start == end: return float('INF')
    
    if end - start == 1: return getDist(points[start], points[end])
    
    mid = (start + end) // 2
    minDist = min(dac(start, mid), dac(mid, end))

    target_pos = []
    for i in range(start, end+1):
        if (points[mid][0] - points[i][0]) ** 2 < minDist:
            target_pos.append(points[i])
    target_pos.sort(key=lambda x : x[1])

    t = len(target_pos)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target_pos[i][1] - target_pos[j][1]) ** 2 < minDist:
                minDist = min(minDist, getDist(target_pos[i], target_pos[j]))
            else:
                break
    return minDist

=======
import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()

def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2

def dac(start, end):
    if start == end: return float('INF')
    
    if end - start == 1: return getDist(points[start], points[end])
    
    mid = (start + end) // 2
    minDist = min(dac(start, mid), dac(mid, end))

    target_pos = []
    for i in range(start, end+1):
        if (points[mid][0] - points[i][0]) ** 2 < minDist:
            target_pos.append(points[i])
    target_pos.sort(key=lambda x : x[1])

    t = len(target_pos)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target_pos[i][1] - target_pos[j][1]) ** 2 < minDist:
                minDist = min(minDist, getDist(target_pos[i], target_pos[j]))
            else:
                break
    return minDist

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(dac(0, N-1))