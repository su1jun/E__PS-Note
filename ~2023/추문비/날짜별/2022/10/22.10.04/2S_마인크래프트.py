import sys
input = sys.stdin.readline

data = []
ans = []

N, M, B = map(int, input().split())
for _ in range(N):
    data += list(map(int, input().split()))
print(f"data : {data}")

top = max(data)
bot = min(data)

for k in range(bot, top+1):
    print(f"k : {k}")
    fil = 0
    dig = 0
    for i in data:
        a = k - i
        if a >= 0:
            fil += a
        else:
            dig -= a
    if fil <= B + dig:
        ans.append([fil*1 + dig*2, k])
ans.sort(key = lambda x : (x[0], -x[1]))
print(f"ans : {ans}")
print(f"{ans[0][0]} {ans[0][1]}")


# from sys import stdin
# from collections import Counter

# def fletten():
#     low = min(arr)
#     high = max(arr)
#     result = [987654321, 0]
    
#     for height in range(low, high+1):
#         block = B
#         sec = 0
#         for h,c in counts.items():
#             gap = h - height
#             block += gap * c
#             if gap > 0:
#                 sec += gap * c * 2
#             elif gap < 0:
#                 sec -= gap * c
#         if block >= 0:
#             if result[0] > sec:
#                 result = [sec,height]
#             elif result[0] == sec and result[1] < height:
#                 result = [sec, height]
        
#     return result

# N, M, B = map(int, stdin.readline().split())
# heights = [0]*257
# arr = []
# for _ in range(N):
#     arr += [*map(int, stdin.readline().split())]

# counts = Counter(arr)
# print(*fletten())