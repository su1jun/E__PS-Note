import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Aj = []
ans = 0
for _ in range(N):
    Aj.append(int(input()))

Aj.reverse()
for i in range(N):
    if M == 0:
        break
    if Aj[i] <= M:
        ans += M // Aj[i]
        M %= Aj[i]
        print(f"Aj[i] : {Aj[i]} / M : {M}")
print(ans)