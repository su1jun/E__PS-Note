import sys
input = sys.stdin.readline
piece = [0 for i in range(11)]
yut = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
[10, 13, 16, 19], [30, 28, 27, 26], [20, 22, 24, 25, 30, 35, 40]]

position = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
[5, 21, 22, 23], [15, 24, 25, 26], [10, 27, 28, 29, 30, 31, 20]]

def score():
    global result
    pi_po = [[0, 0] for i in range(5)]
    num = 0
    for i in range(1, 11):
        pi = piece[i]
        x, y = pi_po[pi]
        if x == -1: return
        else:
            y += s[i]
            if x == 0:
                if 20 < y: pi_po[pi] = [-1, -1]
                elif y == 5: pi_po[pi] = [1, 0]
                elif y == 10: pi_po[pi] = [3, 0]
                elif y == 15: pi_po[pi] = [2, 0]
                else: pi_po[pi] = [x, y]
            elif x == 1:
                if y >= 8: pi_po[pi] = [-1, -1]
                elif y >= 4: pi_po[pi] = [3, y - 1]
                else: pi_po[pi] = [x, y]
            elif x == 2:
                if y >= 8: pi_po[pi] = [-1, -1]
                elif y >= 4: pi_po[pi] = [3, y - 1]
                else: pi_po[pi] = [x, y]
            elif x == 3:
                if y > 6: pi_po[pi] = [-1, -1]
                else: pi_po[pi] = [x, y]
            nx, ny = pi_po[pi]
            if nx != -1:
                for k in range(1, 5):
                    if pi == k: continue
                    a, b = pi_po[k]
                    if a == -1: continue
                    if position[a][b] == position[nx][ny]: return
                num += yut[nx][ny]
    result = max(result, num)
def dfs():
    global depth
    if depth == 10:
        score()
        return
    for i in range(1, 5):
        depth += 1
        piece[depth] = i
        dfs()
        depth -= 1
s = [0] + list(map(int, input().split()))
result = 0
depth = 0
dfs()
print(result)