import sys
input = sys.stdin.readline

def DFS(v): 
    for i in range(1, n+1):
        if board[v][i] == 1 and check[i] == 1 :
            for j in range(1, n+1):
                if check[j] == 1:
                    answer.add(j)
        elif board[v][i] == 1 and check[i] == 0:
            check[i] = 1
            DFS(i)
            check[i] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        board[int(input())][i+1] = 1

    answer = set()
    check = [0] * (n+1)

    for x in range(1, n+1):
        for y in range(1, n+1):
            if board[x][y] == 1 :
                check[x] = 1
                check[y] = 1
                DFS(y)
                check[x] = 0
                check[y] = 0

    answer = list(answer)
    answer.sort()

    print(len(answer))
    for k in answer:
        print(k)