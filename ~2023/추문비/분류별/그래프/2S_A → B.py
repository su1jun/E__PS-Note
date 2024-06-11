# ... 역산?
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0

while N < M:
    if M % 2 == 0:
        M //= 2
        cnt += 1
    elif M % 10 == 1:
        M = str(M)
        M = int(M[:-1])
        cnt += 1
    else:
        break

if N == M:
    print(cnt+1)
else:
    print(-1)