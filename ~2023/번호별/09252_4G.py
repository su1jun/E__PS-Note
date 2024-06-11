<<<<<<< HEAD
input = __import__('sys').stdin.readline

A = input().rstrip()
B = input().rstrip()

aLen = len(A)
bLen = len(B)
dp = [[0] * (aLen+1) for _ in range(bLen+1)]


for i in range(1, bLen+1):
    fd_max = 0
    for j in range(1, aLen+1):
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#print("구분", *dp)

idx_x = bLen
idx_y = aLen
cnt = dp[bLen][aLen]
ans = []
while cnt > 0:
    if dp[idx_x][idx_y] - 1 == dp[idx_x-1][idx_y] == dp[idx_x][idx_y-1]:
        ans.append(A[idx_y-1])
        idx_x -= 1
        idx_y -= 1
        cnt -= 1
    else:
        if dp[idx_x-1][idx_y] > dp[idx_x][idx_y-1]:
            idx_x -= 1
        else:
            idx_y -= 1
print(dp[bLen][aLen])
print("".join(ans[::-1]))
# 0 1 0 0 0 0
# 1 0 2 0 0 0
# 0 0 0 0 0 3
# 0 2 0 0 0 0
# 1 0 3 0 0 0
# 0 0 0 0 4 0

# 1 2 3 0 4 3
=======
input = __import__('sys').stdin.readline

A = input().rstrip()
B = input().rstrip()

aLen = len(A)
bLen = len(B)
dp = [[0] * (aLen+1) for _ in range(bLen+1)]


for i in range(1, bLen+1):
    fd_max = 0
    for j in range(1, aLen+1):
        if B[i-1] == A[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#print("구분", *dp)

idx_x = bLen
idx_y = aLen
cnt = dp[bLen][aLen]
ans = []
while cnt > 0:
    if dp[idx_x][idx_y] - 1 == dp[idx_x-1][idx_y] == dp[idx_x][idx_y-1]:
        ans.append(A[idx_y-1])
        idx_x -= 1
        idx_y -= 1
        cnt -= 1
    else:
        if dp[idx_x-1][idx_y] > dp[idx_x][idx_y-1]:
            idx_x -= 1
        else:
            idx_y -= 1
print(dp[bLen][aLen])
print("".join(ans[::-1]))
# 0 1 0 0 0 0
# 1 0 2 0 0 0
# 0 0 0 0 0 3
# 0 2 0 0 0 0
# 1 0 3 0 0 0
# 0 0 0 0 4 0

# 1 2 3 0 4 3
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
