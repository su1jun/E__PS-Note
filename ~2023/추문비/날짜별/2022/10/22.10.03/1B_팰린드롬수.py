import sys
input = sys.stdin.readline

while True:
    T = str(input().strip())
    if T == "0":
        break
    for i in range(1, len(T)//2 + 1):
        if T[i-1] != T[-i]:
            print("no")
            break
    else:
        print("yes")
