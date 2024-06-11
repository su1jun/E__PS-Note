import sys
input = sys.stdin.readline

W, N = map(str, input().split())
N = int(N)
arr = [list(map(int, input().split())) for _ in range(N)]
mirror = {1:1, 2:5, 5:2, 8:8}

if W == "D" or W == "U":
    for i in arr[::-1]:
        for j in i:
            if j in mirror:
                print(mirror[j], end=" ")
            else:
                print("?", end=" ")
        print()
elif W == "L" or W == "R":
    for i in range(N):
        for j in range(N):
            if arr[i][N-1-j] in mirror:
                print(mirror[arr[i][N-1-j]], end=" ")
            else:
                print("?", end=" ")
        print()