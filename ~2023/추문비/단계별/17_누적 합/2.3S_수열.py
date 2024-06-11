import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, N):
    data[i] += data[i-1]
data = [0] + data
print(f"data : {data}")

for i in range(N-K+1):
    data[i] = data[i+K] - data[i]
data = data[0:N-K+1]
print(f"data : {data}")
print(max(data))