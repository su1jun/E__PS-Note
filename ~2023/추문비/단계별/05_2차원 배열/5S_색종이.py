import sys
input = sys.stdin.readline

paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if x+i < 100 and y+j < 100:
                paper[x+i][y+j] = 1
print(sum(map(sum, paper)))