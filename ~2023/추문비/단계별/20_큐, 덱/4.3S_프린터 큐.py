from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        fd = max(queue)
        hd = queue.popleft()
        M -= 1

        if fd == hd:
            count += 1
            if M < 0:
                print(count)
                break

        else:
            queue.append(hd)
            if M < 0 :
                M = len(queue) - 1