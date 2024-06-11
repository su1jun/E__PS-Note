import sys
input = sys.stdin.readline

N = int(input()) # 탑의 갯수
arr = list(map(int, input().rsplit())) # 탑의 갯수
stack = [[arr[0], 1]]
print(0, end=" ")
for i in range(1, N):
    while stack and stack[-1][0] < arr[i]:
        stack.pop()
    else:
        if not stack:
            print(0, end=" ")
            stack.append([arr[i], i+1])
        elif arr[i] < stack[-1][0]:
            print(stack[-1][1], end=" ")
            stack.append([arr[i], i+1])
        elif arr[i] == stack[-1][0]:
            print(stack[-1][1], end=" ")
            stack[-1][1] = i+1
        


