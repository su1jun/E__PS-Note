import sys
input = sys.stdin.readline

N = int(input())
S = format(N+1, 'b')
S = S[1:]
print(S.replace('0', '4').replace('1', '7'))