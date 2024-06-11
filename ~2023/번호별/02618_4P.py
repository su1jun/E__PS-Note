<<<<<<< HEAD
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def search(row, col):
	# print(row, col)
	# for i in dp:
	# 	print(i)
	# print()
	if row > W or col > W:
		return 0
	if dp[row][col] != -1:
		return dp[row][col]
	next_pos = max(row,col) + 1
	nr = search(next_pos,col) + abs(pos[next_pos][0] - pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = search(row,next_pos) + abs(pos[next_pos][0] - pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])
	dp[row][col] = min(nr,nc)
	return dp[row][col]

def route(row, col):
	if row > W or col > W:
		return
	next_pos = max(row,col) + 1
	nr = abs(pos[next_pos][0] - pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = abs(pos[next_pos][0] - pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])

	if dp[next_pos][col]+nr < dp[row][next_pos]+nc:
		print(1)
		route(next_pos,col)
	else:
		print(2)
		route(row,next_pos)
	return

def solution(N, W):
	print(search(0, 1))
	# for i in dp:
	# 	print(i)
	# print()
	route(0, 1)

N = int(input())
W = int(input())
pos = [(1, 1),(N, N)]
dp = [[-1] * (W+2) for _ in range(W+2)]

for _ in range(W):
    pos.append(tuple(map(int, input().split())))
=======
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def search(row, col):
	# print(row, col)
	# for i in dp:
	# 	print(i)
	# print()
	if row > W or col > W:
		return 0
	if dp[row][col] != -1:
		return dp[row][col]
	next_pos = max(row,col) + 1
	nr = search(next_pos,col) + abs(pos[next_pos][0] - pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = search(row,next_pos) + abs(pos[next_pos][0] - pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])
	dp[row][col] = min(nr,nc)
	return dp[row][col]

def route(row, col):
	if row > W or col > W:
		return
	next_pos = max(row,col) + 1
	nr = abs(pos[next_pos][0] - pos[row][0]) + abs(pos[next_pos][1] - pos[row][1])
	nc = abs(pos[next_pos][0] - pos[col][0]) + abs(pos[next_pos][1] - pos[col][1])

	if dp[next_pos][col]+nr < dp[row][next_pos]+nc:
		print(1)
		route(next_pos,col)
	else:
		print(2)
		route(row,next_pos)
	return

def solution(N, W):
	print(search(0, 1))
	# for i in dp:
	# 	print(i)
	# print()
	route(0, 1)

N = int(input())
W = int(input())
pos = [(1, 1),(N, N)]
dp = [[-1] * (W+2) for _ in range(W+2)]

for _ in range(W):
    pos.append(tuple(map(int, input().split())))
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
solution(N, W)