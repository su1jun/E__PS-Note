import sys
input = sys.stdin.readline

L = int(input())
S = input().strip()
ans = 0
for i in range(L):
    print(f"S[i] : {S[i]} / ord(i) : {ord(S[i])}")
    ans += (ord(S[i])-96)*(31**i)
    ans %= 1234567891
print(ans)