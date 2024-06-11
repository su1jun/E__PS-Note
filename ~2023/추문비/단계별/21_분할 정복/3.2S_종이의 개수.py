import sys
input = sys.stdin.readline

dt = []
v1 = 0 # 0
v2 = 0 # 1
v3 = 0 # -1
N = int(input())

for _ in range(N):
    dt += list(map(int, input().split()))
# print(f"dt : {dt}")
# print(sum(dt))

def f(nums, n):
    global v1
    global v2
    global v3

    if nums.count(0) == n**2:
        v1 += 1
        return

    elif nums.count(-1) == n**2:
        v3 += 1
        return

    elif nums.count(1) == n**2:
        v2 += 1
        return
    
    else:
        nums.append(0)
        k = n//3
        for i in range(3): # 시작 세로
            for j in range(3): #  시작 가로
                a = []
                for x in range(k):
                    a += nums[(n*k*i) + k*j + n*x : (n*k*i) + k*j + n*x + k]
                print(f"k : {k}, i : {i}, j : {j}\na : {a}")
                f(a, k)

f(dt, N)
print(f"{v3}\n{v1}\n{v2}")
