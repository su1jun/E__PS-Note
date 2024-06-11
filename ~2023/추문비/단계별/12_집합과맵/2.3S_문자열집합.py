import sys
str1 = set()
ans = 0

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    str1.add(sys.stdin.readline().rstrip())

for _ in range(M):
    if sys.stdin.readline().rstrip() in str1:
        ans += 1
        
print(ans)