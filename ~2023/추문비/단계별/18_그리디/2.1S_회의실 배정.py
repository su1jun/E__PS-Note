import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x : (x[1], x[0]))

end = data[0][1]
cnt = 1
for i in data[1:]:
    if end <= i[0]:
        end = i[1]
        cnt += 1
print(f"data : {data}")
print(cnt)

