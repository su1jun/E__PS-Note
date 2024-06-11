<<<<<<< HEAD
import sys
from collections import deque
input = sys.stdin.readline

# def bfs(n):
#     que = deque([[n]])
#     while que:
#         lst = que.popleft()
#         if lst[-1] % 3 == 0: que.append(lst + [lst[-1] // 3])
#         if lst[-1] % 2 == 0: que.append(lst + [lst[-1] // 2])
#         if lst[-1] > 1: que.append(lst + [lst[-1] - 1])
#         if lst[-1] == 1:
#             print(len(lst)-1)
#             print(*lst)
#             break

# bfs(int(input()))

N = int(input())
way = {N:-1}
stack = [N]

for temp in stack:
    if temp == 1:
        break

    temp_stack = [temp-1]
    if temp % 3 == 0: temp_stack.append(temp//3)
    if temp % 2 == 0: temp_stack.append(temp//2)
    
    for temp2 in temp_stack:
        if temp2 not in way:
            stack.append(temp2)
            way[temp2] = temp

res = [1]
while res[-1] != N:
    res.append(way[res[-1]])
print(len(res)-1)
=======
import sys
from collections import deque
input = sys.stdin.readline

# def bfs(n):
#     que = deque([[n]])
#     while que:
#         lst = que.popleft()
#         if lst[-1] % 3 == 0: que.append(lst + [lst[-1] // 3])
#         if lst[-1] % 2 == 0: que.append(lst + [lst[-1] // 2])
#         if lst[-1] > 1: que.append(lst + [lst[-1] - 1])
#         if lst[-1] == 1:
#             print(len(lst)-1)
#             print(*lst)
#             break

# bfs(int(input()))

N = int(input())
way = {N:-1}
stack = [N]

for temp in stack:
    if temp == 1:
        break

    temp_stack = [temp-1]
    if temp % 3 == 0: temp_stack.append(temp//3)
    if temp % 2 == 0: temp_stack.append(temp//2)
    
    for temp2 in temp_stack:
        if temp2 not in way:
            stack.append(temp2)
            way[temp2] = temp

res = [1]
while res[-1] != N:
    res.append(way[res[-1]])
print(len(res)-1)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(*res[::-1])