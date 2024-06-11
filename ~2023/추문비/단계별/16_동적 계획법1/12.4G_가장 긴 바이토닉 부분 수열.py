import sys
input = sys.stdin.readline

N = int(input())
dp1 = [0] * 1001
dp2 = [0] * 1001
data = list(map(int, input().split()))
data_r = data[::-1]
up = []
down = []

for i in range(N):
    a = max(dp1[:data[i]]) + 1
    dp1[data[i]] = a
    up.append(a)
    print(f"dp1 : {dp1}") ##

    b = max(dp2[:data_r[i]]) + 1
    dp2[data_r[i]] = b
    down.append(b)
    print(f"dp2 : {dp2}") ##

low = 0
print(f"up : {up}") ##
print(f"down : {down}") ##
for i in range(N):
    k = up[i] + down[N-i-1]
    if low < k:
        low = k
        print(f"{i}번째에서 최대값 갱신 & k : {k} ") ##

print(low-1)

