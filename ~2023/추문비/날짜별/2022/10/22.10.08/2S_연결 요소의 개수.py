import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N, T = map(int, input().split())
cnt = 0
xtoy = dict()
ytox = dict()
stp = []
chk = [i for i in range(1, N+1)]
for _ in range(T):
    a, b = map(int, input().split())
    stp += [a, b]
    if a in xtoy:
        xtoy[a].append(b)
    else:
        xtoy[a] = [b]
    if b in ytox:
        ytox[b].append(a)
    else:
        ytox[b] = [a]

stp = list(set(stp))

def f(n):
    order = []
    if n in stp:
        stp.remove(n)
        chk.remove(n)
        if n in xtoy:
            for i in xtoy[n]:
                order.append(i)
            del xtoy[n]
            print(f"x : {n}를 제거, {i}를 인수로 재귀") ##
            print(f"남은 lst & x : {xtoy} // y : {ytox}") ##
        if n in ytox:
            for i in ytox[n]:
                order.append(i)
            del ytox[n]
            print(f"y : {n}를 제거, {i}를 인수로 재귀") ##
            print(f"남은 lst & x : {xtoy} // y : {ytox}") ##
    for i in list(set(order)):
        f(i)
    return

while stp:
    f(stp[0])
    cnt += 1
    print(f"{cnt}회 제거됨, 남은 원소 {stp}") ##
print(cnt+len(chk))