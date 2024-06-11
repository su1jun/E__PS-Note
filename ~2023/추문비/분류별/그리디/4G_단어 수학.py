import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 단어의 갯수
alp = dict() # 알파벳 정보

for _ in range(N):
    s = input().rstrip()
    l = len(s)
    for i in range(l):
        if s[i] in alp:
            alp[s[i]] += 10**(l-i-1)
        else:
            alp[s[i]] = 10**(l-i-1)

lst = sorted(list(alp.values()))
ans = 0
start = 9-len(lst)
for i in lst:
    ans += i*(start+1)
    start += 1
print(ans)