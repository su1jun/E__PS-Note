import sys
input = sys.stdin.readline 

alp = [[0, False] for _ in range(10)]
ans = 0
for _ in range(int(input())):
    s = input().rstrip()
    m = 1
    alp[ord(s[0])-65][1] = True
    for c in range(len(s)-1, -1, -1):
        alp[ord(s[c])-65][0] += m
        m *= 10

alp.sort(reverse=True)
if alp[9][1]:
    for i in range(8, -1, -1):
        if not alp[i][1]:
            del alp[i]
            break
for i in range(9):
    ans += alp[i][0] * (9-i)

print(ans)