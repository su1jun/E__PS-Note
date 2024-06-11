import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
ori = P
S = list(map(int, input().split()))
G = [0, 1, 2] * (N // 3)
new = [0] * N
cnt = 0
 
while P != G:
    for i in range(N):
        new[S[i]] = P[i]
 
    P = new
    new = [0] * N
    cnt += 1
    if ori == P:
        cnt =- 1
        break
print(cnt)