import sys
input = sys.stdin.readline

N = int(input())
data = []
ans = []
for _ in range(N):
    data.append(list(map(int, input().split())))

def f(lst1):
  if len(lst1) == N // 2:
    print(f"lst1 : {lst1}")
    ans.append(c(lst1))
    return

  for i in range(N):
    if i in lst1:
        continue
    if len(lst1) > 0:
        if lst1[-1] < i:
            f(lst1 + [i])
    else:
        f(lst1 + [i])

def c(lst):
    s1 = 0
    s2 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i in lst and j in lst:
                s1 += data[i][j]
            elif i not in lst and j not in lst:
                s2 += data[i][j]
    return abs(s1-s2)

f([])
print(f"ans : {ans}")
print(min(ans))