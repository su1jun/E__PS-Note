import sys

A, B = map(int, sys.stdin.readline().split())
X = max(A, B)
Y = min(A, B)

if X % Y == 0:
    print(Y)
else:
    LCM = Y - 1
    while X % LCM + Y % LCM != 0:
        LCM -= 1
    print(LCM)

GCD = 1
while A * GCD % B != 0:
    GCD += 1
print(A * GCD)