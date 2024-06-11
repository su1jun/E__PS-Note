import sys
dic = {}
str1 = set()
str2 = set()

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    str1.add(sys.stdin.readline().rstrip())

for _ in range(M):
    str2.add(sys.stdin.readline().rstrip())

ans = list(str1 & str2)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
