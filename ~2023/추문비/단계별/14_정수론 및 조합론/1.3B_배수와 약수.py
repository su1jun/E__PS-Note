import sys
A, B = map(int, sys.stdin.readline().split())

while A + B != 0:
    if A % B == 0:
        print("multiple")
    elif B % A == 0:
        print("factor")
    else:
        print("neither")
    A, B = map(int, sys.stdin.readline().split())
