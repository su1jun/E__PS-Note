import sys
n = int(sys.stdin.readline())
ns = set(map(int, sys.stdin.readline().split()))

ns = list(ns)
ns.sort()
print(" ".join([str(i) for i in ns]))
