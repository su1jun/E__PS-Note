import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
data = dict()
s = len(S)
for i in alp:
    data[i] = [0 for _ in range(s+1)]
    for j in range(1, s+1):
        if i == S[j-1]:
            data[i][j] = data[i][j-1] + 1
        else:
            data[i][j] = data[i][j-1]
print(f"data : {data}")
for _ in range(q):
    alr = input().split()
    print(data[alr[0]][int(alr[2])+1]-data[alr[0]][int(alr[1])])

import sys
input = sys.stdin.readline

s = input().rstrip()
d = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    x = ord(s[i - 1]) - ord("a")
    for j in range(26):
        if j == x:
            d[i][j] = d[i - 1][j] + 1
            continue
        d[i][j] = d[i - 1][j]

n = int(input())
for _ in range(n):
    x, l, r = input().rstrip().split()
    x = ord(x) - ord("a")
    r = int(r)
    l = int(l)

    ans = d[r + 1][x] - d[l][x]
    sys.stdout.write(str(ans) + "\n")
