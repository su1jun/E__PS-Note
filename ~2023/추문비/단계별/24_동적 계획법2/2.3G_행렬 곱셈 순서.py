import sys
input = sys.stdin.readline

# 초기 설정
N = int(input())
data = []

for _ in range(N-1):
    r, c = map(int, input().split())
    data.append(r)
data += list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 계산 진행 
# j = len

for i in range(N): ## j = 1
    dp[i][i+1] = data[i]*data[i+1]

for i in range(N-1): ## j = 2
    dp[i][i+2] = data[i+2]*dp[i][i+1]

for j in range(3, N+1): # j >= 3
    # j = 2 일때 따로 계산

    # j > 2
    for i in range(N+1-j): # i = row
        m = 1e9

        # k = 최소값 계산 반복변수
        k = i+1 # 처음부분
        a = dp[i][k]*data[i+j] + dp[k][i+j]
        if m > a:
            m = a

        k = i+j-1 # 끝부분
        a = dp[i][k] + dp[k][i+j]*data[i]
        if m > a:
            m = a
        
        for k in range(i+2, i+j-1):
            a = dp[i][k] + dp[k][i+j] + data[i]*data[k]*data[i+j]
            if m > a:
                m = a
        dp[i][i+j] = m

print(dp[0][N])