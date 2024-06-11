import sys
dict = dict()

N, M = map(int, sys.stdin.readline().split())

for i in range(1, N + 1):
    X = sys.stdin.readline().rstrip()
    dict[str(i)] = X
    dict[X] = i
    
for _ in range(M):
    print(dict[sys.stdin.readline().rstrip()])

        