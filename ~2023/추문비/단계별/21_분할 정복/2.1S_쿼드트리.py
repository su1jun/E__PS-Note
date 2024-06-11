import sys
input = sys.stdin.readline

dt = []
ans = ""
N = int(input())

for _ in range(N):
    NN = list(input().rstrip())
    for i in NN:
        dt.append(int(i))
#print(f"dt : {dt}")
#print(sum(dt))

def f(nums, n):
    global ans

    if sum(nums) == n**2:
        ans += "1"
        return

    elif sum(nums) == 0:
        ans += "0"
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
#        print(f"k : {k}\na : {a}\nb : {b}\nc : {c}\nd : {d}\n")
        ans += "("
        f(a, k)
        f(b, k)
        f(c, k)
        f(d, k)
        ans += ")"

f(dt, N)
print(f"{ans}")
    
