import sys
input = sys.stdin.readline

def t(idx):
    if len(tmp) == M:
        ans.add(tuple(tmp))
        return

    for i in range(N):
        if vst[i]:
            continue

        tmp.append(arr[i])
        vst[i] = 1
        t(idx+1)

        vst[i] = 0
        tmp.pop()
        
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
vst = [0]*N
tmp,ans = [], set()

t(-1)
for i in sorted(ans):
    print(*i)