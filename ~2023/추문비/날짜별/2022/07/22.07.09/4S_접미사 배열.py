import sys

n = str(sys.stdin.readline())
strings = []
i = 0
while i < len(n)-1:
    strings.append(n[i:len(n)-1])
    i += 1
print("\n".join(sorted(strings)))
