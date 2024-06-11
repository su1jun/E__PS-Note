import sys
input = sys.stdin.readline

dt = []
blue = 0
white = 0
N = int(input())

for _ in range(N):
    dt += list(map(int, input().split()))
print(f"dt : {dt}")
print(sum(dt))

def f(nums, n):
    global blue
    global white

    if sum(nums) == n**2:
        blue += 1
        return

    elif sum(nums) == 0:
        white += 1
        return
    
    else:
        a = []
        b = []
        c = []
        d = []
        nums.append(0)
        k = n//2
        for i in range(k):
            a += nums[n*i : n*i + k]
            b += nums[n*i + k : n*(i+1)]
            c += nums[n*(i+k) : n*(i+k) + k]
            d += nums[n*(i+k) + k : n*(i+k+1)]
        print(f"k : {k}\na : {a}\nb : {b}\nc : {c}\nd : {d}\n")
        f(a, k)
        f(b, k)
        f(c, k)
        f(d, k)

f(dt, N)
print(f"{white}\n{blue}")
    
