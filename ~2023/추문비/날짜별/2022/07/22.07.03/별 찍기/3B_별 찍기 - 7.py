import sys
n = int(sys.stdin.readline())

for i in range(n):
    print(' '*i + '*'*(2 * (n - i) - 1))