import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost.pop()
ans = 0

# while cost:
#     low = min(cost)
#     low_idx = cost.index(low)
#     ans += sum(length[low_idx:])*low
#     length = length[:low_idx]
#     cost = cost[:low_idx]

# print(ans)

low = cost[0]
ans = length[0]*cost[0]
for i in range(1, N-1):
    if cost[i] < low:
        low = cost[i]
    ans += low*length[i]
print(ans)


