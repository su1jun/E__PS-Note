import sys
A = set()
cnt = 2

string = sys.stdin.readline().rstrip()
A.add(string)

for i in string:
    A.add(i)

l = len(string)
while cnt != l:
    for i in range(l - cnt + 1):
        if i + cnt > l:
            A.add(string[i:])
        else:
            A.add(string[i:i+cnt])
    cnt += 1

print(len(A))

