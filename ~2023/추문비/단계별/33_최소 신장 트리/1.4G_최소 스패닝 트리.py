import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N 

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

m_val = max(dp)
print(m_val)

ans = []
for i in range(N-1, -1, -1):
    if dp[i] == m_val:
        ans.append(arr[i])
        m_val -= 1

ans.reverse()
print(*ans)