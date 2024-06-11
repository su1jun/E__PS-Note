import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

for i in range(1, N):
    data[i] += data[i-1]
data = [0] + data
print(f"data : {data}")
for _ in range(M):
    st, ed = map(int, input().split())
    print(data[ed] - data[st-1])