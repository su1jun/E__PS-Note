import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

chk = False
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        chk = True
        break

if chk:
    print(1)
else:
    print(0)

