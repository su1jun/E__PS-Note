import re
import sys
input = sys.stdin.readline

T = int(input())
ans = []
 
for _ in range(T):
    sign = input().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m: ans.append("YES")
    else: ans.append("NO")
 
for i in ans:
    sys.stdout.write(str(i)+'\n')
