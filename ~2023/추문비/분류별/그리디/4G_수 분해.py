# 두수의 곱이 합을 초과하는 시점
import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 단어의 갯수
C = 10007
if N < 5:
    print(N)
else:
    num = [2, 3, 4]
    idx = (N-2) % 3
    k = (N-2) // 3
    for i in range(k):
        num[idx] *= 3
        num[idx] %= C
    print(num[idx])