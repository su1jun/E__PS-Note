import sys

n = int(sys.stdin.readline())
ns= [1, 1]
i = 1
while i <= n-2:
	ns.append(ns[i-1] + ns[i])
	i += 1
print(ns[-1], n-2)