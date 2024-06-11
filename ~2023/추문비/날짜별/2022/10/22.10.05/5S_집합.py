import sys
input = sys.stdin.readline
print = sys.stdout.write

M = int(input())
S = set()
for _ in range(M):
    cmd = list(map(str, input().split()))
    if cmd[0] == "add":
        S.add(cmd[1])
    elif cmd[0] == "remove":
        S.discard(cmd[1])
    elif cmd[0] == "check":
        if cmd[1] in S:
            print("1\n")
        else:
            print("0\n")
    elif cmd[0] == "toggle":
        if cmd[1] in S:
            S.discard(cmd[1])
        else:
            S.add(cmd[1])
    elif cmd[0] == "all":
        S.update([str(i) for i in range(1, 21)])
    else:
        S = set()