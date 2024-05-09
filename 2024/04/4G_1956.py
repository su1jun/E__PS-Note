import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
matrix = [[INF] * (V+1) for _ in range(V+1)]

def floydWarshall():
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                                   
    answer = INF
    for i in range(1, V+1):
        answer = min(answer, matrix[i][i])

    if answer == INF:
        return -1
    else:
        return answer

for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = min(c, matrix[a][b])

print(floydWarshall())