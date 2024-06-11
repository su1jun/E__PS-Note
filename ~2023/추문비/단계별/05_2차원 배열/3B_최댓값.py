import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]
max_row = 0
max_col = 0
max_val = 0

for i in range(9):
    for j in range(9):
        if max_val < matrix[i][j]:
            max_val = matrix[i][j]
            max_row = i
            max_col = j
print(max_val)
print(max_row + 1, max_col + 1)