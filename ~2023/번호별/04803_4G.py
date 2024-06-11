<<<<<<< HEAD
import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x 
    else:
        parents[x] = y

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

case = 0
while True:
    case += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0: break

    parents = [i for i in range(N+1)]
    cycle = set()
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) == find(b):
            cycle.add(parents[a])
            cycle.add(parents[b])
        if parents[a] in cycle or parents[b] in cycle:
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a, b)

    for i in range(N+1):
        find(i)

    parents = set(parents)
    ans = sum([1 if i not in cycle else 0 for i in parents]) - 1
    if ans == 0:
        print(f"Case {case}: No trees.")
    elif ans == 1:
        print(f"Case {case}: There is one tree.")
    else:
=======
import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x 
    else:
        parents[x] = y

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

case = 0
while True:
    case += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0: break

    parents = [i for i in range(N+1)]
    cycle = set()
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) == find(b):
            cycle.add(parents[a])
            cycle.add(parents[b])
        if parents[a] in cycle or parents[b] in cycle:
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a, b)

    for i in range(N+1):
        find(i)

    parents = set(parents)
    ans = sum([1 if i not in cycle else 0 for i in parents]) - 1
    if ans == 0:
        print(f"Case {case}: No trees.")
    elif ans == 1:
        print(f"Case {case}: There is one tree.")
    else:
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
        print(f"Case {case}: A forest of {ans} trees.")