import sys, collections
input = sys.stdin.readline

N = int(input())
log = collections.defaultdict(int)

for _ in range(N):
    a, b = input().rstrip().split()
    
    if b == 'enter':
        log[a] += 1
    else:
        log[a] -= 1

filtered = [k for k, v in log.items() if v > 0]
log = sorted(filtered, reverse=True)

print('\n'.join(log))