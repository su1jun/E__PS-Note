import sys
input = sys.stdin.readline

# 초기 입력 설정
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.append(0)

# 실행
ans = 0
area = 0
stack = [[0,  0]] # stack[i][0] = idx, stack[i][1] = height
for i in range(0, N+1):
    if data[i] < stack[-1][1]:
        while data[i] < stack[-1][1]:
            [idx, h] = stack.pop()
            area = (i - idx)*h # area = 넓이
            if ans < area:
                ans = area # 최고값 갱신
        stack.append([idx, data[i]])
    if data[i] > stack[-1][1]:
        stack.append([i, data[i]])
print(ans)