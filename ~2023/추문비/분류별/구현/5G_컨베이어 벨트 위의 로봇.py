import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
ans = 0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    if sum(robot):
        for i in range(N-2, -1, -1): 
            if robot[i] and not robot[i+1] and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1] = 0

    if not robot[0] and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    ans += 1

    if belt.count(0) >= K:
        break
                
print(ans)