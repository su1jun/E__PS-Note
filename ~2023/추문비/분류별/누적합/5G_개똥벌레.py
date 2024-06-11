import sys
input = sys.stdin.readline
N, H = map(int, input().split())

down = [0] * (H+1)  # 석순
up = [0] * (H+1)  # 종유석

min_count = N  # 파괴해야 하는 장애물의 최소값
range_count = 0  # 최소값이 나타나는 구간의 수

for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(H - 1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, H+1):

    if min_count > (down[i] + up[H-i + 1]):
        min_count = (down[i] + up[H-i + 1])
        range_count = 1
    elif min_count == (down[i] + up[H-i + 1]):
        range_count += 1

print(min_count, range_count)