import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))
cnt = [0] * M
data[0] %= M
cnt[data[0]] += 1
for i in range(1, N):
    data[i] += data[i-1]
    data[i] %= M
    cnt[data[i]] += 1
print(f"cnt : {cnt}")
ans = cnt[0]*(cnt[0]+1)//2
for i in cnt[1:]:
    if i < 1:
        continue
    ans += (i-1)*i // 2
print(f"data : {data}")
print(ans)
