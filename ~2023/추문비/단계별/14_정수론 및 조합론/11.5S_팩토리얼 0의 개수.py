import sys

def fct(N):
    if N <= 1:
        return 1
    else:
        return N * fct(N-1)

chk = str(fct(int(sys.stdin.readline())))
if chk[-1] == '0':
    ans = 1
    while chk[-(ans+1)] == '0':
        ans +=1
    print(ans)
else:
    print(0)
