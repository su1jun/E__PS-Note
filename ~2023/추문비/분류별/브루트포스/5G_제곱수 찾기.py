import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, list(input().replace('\n', '')))) for _ in range(M)]
num = ["0", "1", "4", "5", "6", "9"]
res = -1

for i in range(M): # 행 시작
    for j in range(N): # 열 시작
        for step_i in range(-M, M): # 행 공차
            for step_j in range(-N, N): # 열 공차
                if step_i == 0 and step_j == 0: continue
                step = 0
                x = i
                y = j
                val = ''
                while (0 <= x < M) and (0 <= y < N):
                    val += str(arr[x][y])
                    step += 1

                    if val[-1] in num:
                        val_int = int(''.join(val))
                        val_sqrt = math.sqrt(val_int)
                        val_dec = val_sqrt - int(val_sqrt)
                        if val_dec == 0 and val_int > res: res = val_int

                    x = i + step * step_i
                    y = j + step * step_j

print(res)

'''
1 > 1
2 > 4
3 > 9
4 > 6
5 > 5
6 > 6
7 > 9
8 > 4
9 > 1
0, 1, 4, 5, 6, 9
'''