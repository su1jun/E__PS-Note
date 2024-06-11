import sys
n = int(sys.stdin.readline())
ns = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))

for i in ms:
    if i in ns:
        print(1)
    else:
        print(0)
