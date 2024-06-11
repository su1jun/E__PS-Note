import sys
input = sys.stdin.readline

s1 = input().strip()
s1 = s1.split("-")

s2 = []
for i in s1:
    print(type(i.split('+')))
    print(f"i.split(+) : {i.split('+')}")
    s2.append(sum(list(map(int, i.split('+')))))
ans = s2[0] - sum(s2[1:])
print(ans)