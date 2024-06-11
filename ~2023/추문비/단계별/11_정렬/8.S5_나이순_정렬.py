import sys
N = int(sys.stdin.readline())
p = []

for _ in range(N):
    A, B = map(str, sys.stdin.readline().split())
    p.append([A, B])

p.sort(key=lambda x:(int(x[0])))

for x, y in p:
    print(x, y, sep=" ")