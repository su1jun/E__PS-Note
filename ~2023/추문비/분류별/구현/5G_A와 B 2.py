# 백트래킹, 그냥 다해보기
import sys
input = sys.stdin.readline

def chkab(c):
    global chk

    if len(c) == len(S):
        if c == S:
            chk = True

        return

    if c[0] == "B":
        c.reverse()
        c.pop()
        chkab(c)
        c.append("B")
        c.reverse()

    if c[-1] == "A":
        c.pop()
        chkab(c)
        c.append("A")

S = list(input().rstrip())
T = list(input().rstrip())
chk = False
chkab(T)

if chk:
    print(1)
else:
    print(0)