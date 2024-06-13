import sys
input = sys.stdin.readline

N = int(input())
Arr = list(map(int, input().split()))
Brr = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

answer = []
for i in range(N):
    if Arr[i] == 0:
        answer.append(Brr[i])
answer.reverse()

if answer == []:
    print(*C)
else:
    if M > len(answer):
        for j in range(M - len(answer)):
            answer.append(C[j])
        print(*answer)
    else:
        print(*answer[0:M])