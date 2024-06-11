import sys
input = sys.stdin.readline

def solution(s):
    x = 0
    for c in s:
        if x < 0:
            break
        x = x+1 if c=="(" else x-1 if c==")" else x
    return x == 0

S = input().rstrip()
print(solution(S))