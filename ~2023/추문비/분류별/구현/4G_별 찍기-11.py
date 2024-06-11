import sys
input = sys.stdin.readline

N = int(input())
graph = [[' '] * 2 * N for _ in range(N)]

def draw(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        for i in range(-2, 3):
            graph[x+2][y+i] = '*'
    else:
        nextN = N // 2
        draw(x, y, nextN)
        draw(x + nextN, y - nextN, nextN)
        draw(x + nextN, y + nextN, nextN)

draw(0, N - 1, N)
for i in graph:
    print("".join(i))