import sys
input = sys.stdin.readline

def backtracking(k):
    global group
    print(*lst)
    if k == N:
        group.add("".join(map(str, lst)))
        return
    
    else:
        for i in range(1, N+1):
            if lst[i] < i:
                lst[i] += 1
                backtracking(k+1)
                lst[i] -= 1

N = int(input())
lst = [0] * (N+1)
group = set()

backtracking(0)
print(len(group))
