import sys
input = sys.stdin.readline

N = int(input())
dancer = {'ChongChong'}

for i in range(1, N+1):
    a, b = input().rstrip().split()

    if a in dancer: dancer.add(b)

    if b in dancer: dancer.add(a)

print(len(dancer))