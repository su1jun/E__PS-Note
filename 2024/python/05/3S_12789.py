import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = []
turn = 1

for i in range(N):
    if nums[i] == turn:
        turn += 1
    else:
        stack.append(nums[i])

    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

if stack:
    print("Sad")
else:  
    print("Nice")