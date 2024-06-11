import sys
input = sys.stdin.readline

# Y 2, F 3, O 4
N, G = map(str, input().split()) # G 게임 종류
N = int(N)
arr = set([input().rstrip() for _ in range(N)])
l = len(arr)

game = {"Y":1, "F":2, "O":3}
print(l//game[G])