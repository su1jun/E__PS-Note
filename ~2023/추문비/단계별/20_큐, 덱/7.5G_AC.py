from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    rtq = deque(input().rstrip().strip('[]').split(','))
    print(f"입력 확인용 : {rtq}")

    Rcnt = 0
    for i in p:
        if i == "R":
            Rcnt += 1
        else:
            if n:
                if Rcnt % 2 == 0:
                    rtq.popleft()
                else:
                    rtq.pop()
                n -= 1
            else:
                print("error")
                break
    else:
        if Rcnt % 2 != 0:
            rtq.reverse()

        rtq = '[' + ','.join(list(rtq)) +']'
#        print(f"#####결과 : {rtq}")
        print(rtq)