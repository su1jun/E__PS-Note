import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 출력할 줄
tmp = list(input().rstrip())
board = []
board.append(tmp.copy())

tmp = [[tmp.copy()], [tmp.copy()]]

for i in range(N-1):
    for j in range(N):

        if board[-1][j] == "#": # 현재 칸
            if tmp[-2][j] == "#":
                tmp[-2][j] = "."
            else:
                tmp[-2][j] = "#"

            if j > 0: # 왼쪽 칸
                if tmp[-2][j-1] == "#":
                    tmp[-2][j-1] = "."    
                else:
                    tmp[-2][j-1] = "#"    

            if j < N-1: # 오른쪽 칸
                if tmp[-2][j+1] == "#":
                    tmp[-2][j+1] = "."    
                else:
                    tmp[-2][j+1] = "#" 

            if i < N-1: # 아래칸
                tmp[-1][j+1] = "#" 
    
    board.append(tmp.copy())

    for j in range(N):
        tmp[j]

    print(f"{i+1}번째 {tmp}")
    
    


print(board)






