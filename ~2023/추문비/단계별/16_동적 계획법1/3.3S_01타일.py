import sys
input = sys.stdin.readline

# N = int(input())

# db = [0 for _ in range(N)]
# db[0] = 1
# if N > 1:
#     db[1] = 2
#     for i in range(2, N):
#         db[i] = db[i-1] % 15746 + db[i-2] % 15746
#     print(f"{db[N-1] % 15746}")
# else:
#     print(1)

n = int(input())
left,right = 1,2
D = 15746
for i in range(3,n+1):
    left,right = right % D, (left + right) % D
if n == 1:
    print(1)
else:
    print(right)