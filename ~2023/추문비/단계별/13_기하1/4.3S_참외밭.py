import sys
dic = {}
dic2 = {}
tick = ""
tock = []

K = int(sys.stdin.readline())
for _ in range(6):
    A, B = map(int, sys.stdin.readline().split())
    tick += str(A)
    tock.append(B)
    if A in dic:
        dic2[A] = B
    else:
        dic[A] = B

tick += tick
cnt = 0
chk = tick[:4]
while chk[0] != chk[2] or chk[1] != chk[3]:
    cnt += 1
    chk = tick[cnt:cnt+4]


print("chk:", chk)
print("cnt:", cnt)
print("tock:", tock)

N = 1
for i in range(1, 5):
    if i not in dic2:
        N *= dic[i]
M = tock[(cnt+1)%6] * tock[(cnt+2)%6]

print((N - M)*K)

