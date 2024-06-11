<<<<<<< HEAD
import sys
input = sys.stdin.readline

def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]
 
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False
     
def convex_hull(pos):
    convex = []
    for p3 in pos:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
     
    return len(convex)
 
N, ans = int(input()), -2
pos = [list(map(int, input().split())) for _ in range(N)]

pos = sorted(pos, key=lambda pos:(pos[0], pos[1]))
ans += convex_hull(pos)
 
pos.reverse()
ans += convex_hull(pos)
print(ans)


=======
import sys
input = sys.stdin.readline

def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]
 
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False
     
def convex_hull(pos):
    convex = []
    for p3 in pos:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
     
    return len(convex)
 
N, ans = int(input()), -2
pos = [list(map(int, input().split())) for _ in range(N)]

pos = sorted(pos, key=lambda pos:(pos[0], pos[1]))
ans += convex_hull(pos)
 
pos.reverse()
ans += convex_hull(pos)
print(ans)


>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
