import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
ans = 0

P.sort()

print(f"P : {P}")
for i in range(N):
    ans += P[i]*(N-i)
print(ans)