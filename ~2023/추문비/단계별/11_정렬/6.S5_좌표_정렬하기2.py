import sys
N = int(sys.stdin.readline())
p = []

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    p.append([A, B])

p.sort(key=lambda x:(x[1], x[0]))

for x, y in p:
    print(x, y, sep=" ")