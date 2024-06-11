#$ 인덱스 논리, i-1 값을 i로 옮겨서 순서유지 $#
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

cnt = 0
l = [0 for _ in T]
T_set = set(T)

for x in S:
    if x in T_set:
        if x == T[0]: # idx = 0
            l[0] += 1
        else:
            idx = T.find(x) # t[idx] = x
            if l[idx - 1]:
                l[idx - 1] -= 1
                l[idx] += 1

print(l[-1])