import sys
input = sys.stdin.readline
# int(input())
# input().rstrip()
# map(int, input().split())
# list(map(int, input().split()))
# [for _ in range()]

grid = [[True] * 10 for _ in range(10)]
#print(grid[3:6][2])
grid[3:6][2] = False
for i in grid:
    print(*i)
print()
grid[4] = [False for i in range(10)]
for i in grid:
    print(*i)