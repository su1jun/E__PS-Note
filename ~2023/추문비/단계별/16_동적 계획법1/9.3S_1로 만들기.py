import sys
input = sys.stdin.readline

n = int(input())

def clc(n):
    s = [n-1]
    if n % 2 == 0:
        s.append(n//2)
    if n % 3 == 0:
        s.append(n//3)
    # print(f"s : {s}")
    return s

dp = [n]
cnt = 0
# print(f"dp : {dp}")
# print(f"dp type : {type(dp)}")
while True:
    if 1 in dp:
        break
    cnt += 1
    s = []
    for j in dp:
        # print(f"j : {j}")
        s += clc(j)
    dp = s.copy()
print(cnt)