import sys
input = sys.stdin.readline

while True:
    # 초기 입력 설정
    data = list(map(int, input().split()))
    data.append(0)
    n = data[0]
    if n == 0:
        break
    
    # 실행
    ans = 0
    area = 0
    stack = [[0,  0]] # stack[i][0] = idx, stack[i][1] = height
    for i in range(1, n+2):
        if data[i] < stack[-1][1]:
            while data[i] < stack[-1][1]:
                [idx, h] = stack.pop()
                area = (i - idx)*h # area = 넓이
                if ans < area:
                    ans = area # 최고값 갱신
            stack.append([idx, data[i]])
        if data[i] > stack[-1][1]:
            stack.append([i, data[i]])
        print(f"i : {i}, stack : {stack}, area : {area}, ans : {ans}")
    print(ans)
