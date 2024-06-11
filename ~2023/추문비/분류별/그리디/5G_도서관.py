import sys
input = sys.stdin.readline

def runing(lst):
    l = len(lst)
    cnt = l % M
    sum = 0
    if cnt == 0:
        for i in range(M-1, l, M):
            sum += 2*abs(lst[i])
    else:
        for i in range(cnt-1, l, M):
            sum += 2*abs(lst[i])
    return sum

#초기 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))
minus = []
plus = []
for i in arr:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)

minus.sort(reverse=True)
plus.sort()
ans = runing(minus) + runing(plus)
if minus and plus:
    ans -= max(abs(minus[-1]), plus[-1])
elif minus:
    ans -= abs(minus[-1])
else:
    ans -= plus[-1]

print(ans)