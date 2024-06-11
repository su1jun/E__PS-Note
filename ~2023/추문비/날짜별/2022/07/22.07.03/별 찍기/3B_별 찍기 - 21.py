import sys
n = int(sys.stdin.readline())

for i in range(1, 2*n+1):
    if i % 2 == 0:
        print(' *'*(n//2))
    else:
        if n % 2 == 0:
            print('* '*(n//2))
        else:
            print('* '*(n//2+1))