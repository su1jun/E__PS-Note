<<<<<<< HEAD
# 뮤탈리스크
import sys
from itertools import permutations
input = sys.stdin.readline

def answer(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        if ans > cnt:
            ans = cnt
            return

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    for i, j, k in permutations([9, 3, 1], 3):
        answer(x-i, y-j, z-k, cnt+1)

N = int(input())
arr = list(map(int, input().split()))
while len(arr) < 3:
    arr += [0]
ans = 100
dp = [[[100] * (max(arr)+1) for _ in range((max(arr)+1))] for _ in range((max(arr)+1))]
answer(arr[0], arr[1], arr[2], 0)
=======
# 뮤탈리스크
import sys
from itertools import permutations
input = sys.stdin.readline

def answer(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        if ans > cnt:
            ans = cnt
            return

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    for i, j, k in permutations([9, 3, 1], 3):
        answer(x-i, y-j, z-k, cnt+1)

N = int(input())
arr = list(map(int, input().split()))
while len(arr) < 3:
    arr += [0]
ans = 100
dp = [[[100] * (max(arr)+1) for _ in range((max(arr)+1))] for _ in range((max(arr)+1))]
answer(arr[0], arr[1], arr[2], 0)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans)