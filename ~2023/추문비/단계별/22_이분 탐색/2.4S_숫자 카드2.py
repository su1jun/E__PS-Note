import sys
dic = {}

N = int(sys.stdin.readline())
num1 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
num2 = map(int, sys.stdin.readline().split())

for i in num1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = ''
for i in num2:
    if i in dic:
        ans += str(dic[i]) + ' '
    else:
        ans += '0 '
print(ans.rstrip())