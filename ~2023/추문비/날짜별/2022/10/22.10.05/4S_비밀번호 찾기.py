import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
pswd = dict([])
for _ in range(N):
    a, b = map(str, input().split())
    pswd[a] = b
for _ in range(M):
    find = input().rstrip()
    print(f"{pswd[find]}\n")