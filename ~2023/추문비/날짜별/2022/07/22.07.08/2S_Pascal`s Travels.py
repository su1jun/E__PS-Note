import sys

n = int(sys.stdin.readline())
while n != -1:
    board = [0] * n
    for i in range(n):
        board[i] = [i for i in str(sys.stdin.readline())]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            l = int(board[i][j])
            if l != 0:
                if i+l < n:
                    dp[i+l][j] += dp[i][j]
                if j+l < n:
                    dp[i][j+l] += dp[i][j]
    print(dp[-1][-1])
    n = int(sys.stdin.readline())

