<<<<<<< HEAD
import sys
input = sys.stdin.readline

N = int(input())
log = set()
ans = 0
for _ in range(N):
    s = input().rstrip()
    if s != "ENTER":
        log.add(s)
    else:
        ans += len(log)
        log = set()
ans += len(log)
=======
import sys
input = sys.stdin.readline

N = int(input())
log = set()
ans = 0
for _ in range(N):
    s = input().rstrip()
    if s != "ENTER":
        log.add(s)
    else:
        ans += len(log)
        log = set()
ans += len(log)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(ans)