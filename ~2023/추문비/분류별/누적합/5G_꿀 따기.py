from copy import deepcopy

N = int(input())
H = list(map(int, input().split()))
S = deepcopy(H)
ans=0

for i in range(1, N):
    S[i] += S[i-1]

for i in range(1, N-1):
    ans = max(ans, 2*S[-1]-H[0]-H[i]-S[i])
for i in range(1, N-1):
    ans = max(ans, S[-1]-H[-1]-H[i]+S[i-1])
for i in range(1, N-1):
    ans = max(ans, S[i]-H[0] + S[-1]-S[i-1]-H[-1])

print(ans)