import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
ans = []
dt = [[] for _ in range(N+1)]
for _ in range(T):
    a, b = map(int, input().split())
    dt[a].append(b)
    dt[b].append(a)

print(dt) ##

def f(nums):
    global ans
    for i in nums:
        if i not in ans:
            c = dt[i]
            print(f"c : {c}") ##
            ans.append(i)
            if c:
                f(c)
            else:
                return
f([1])
print(f"set(ans) : {set(ans)}") ##
print(len(set(ans))-1)