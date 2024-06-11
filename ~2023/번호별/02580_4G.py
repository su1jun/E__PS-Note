<<<<<<< HEAD
import sys
input = sys.stdin.readline

def backtracking(n):
    if n == len(blank):
        for i in graph:
            print(*i, sep="")
        sys.exit()
        
    x, y = blank[n]
    a, b = x//3 * 3, y//3 * 3
    cand2 = cand[:]
    
    for i in range(a, a+3):
        for j in range(b, b+3):
            if graph[i][j] in cand2:
                cand2.remove(graph[i][j])
    
    for i in range(9):
        if graph[x][i] in cand2:
            cand2.remove(graph[x][i])
        if graph[i][y] in cand2:
            cand2.remove(graph[i][y])
    
    for i in cand2:
        graph[x][y] = i
        backtracking(n+1)
    graph[x][y] = 0

graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if not graph[i][j]]
cand = [i for i in range(1, 10)]
=======
import sys
input = sys.stdin.readline

def backtracking(n):
    if n == len(blank):
        for i in graph:
            print(*i, sep="")
        sys.exit()
        
    x, y = blank[n]
    a, b = x//3 * 3, y//3 * 3
    cand2 = cand[:]
    
    for i in range(a, a+3):
        for j in range(b, b+3):
            if graph[i][j] in cand2:
                cand2.remove(graph[i][j])
    
    for i in range(9):
        if graph[x][i] in cand2:
            cand2.remove(graph[x][i])
        if graph[i][y] in cand2:
            cand2.remove(graph[i][y])
    
    for i in cand2:
        graph[x][y] = i
        backtracking(n+1)
    graph[x][y] = 0

graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if not graph[i][j]]
cand = [i for i in range(1, 10)]
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
backtracking(0)