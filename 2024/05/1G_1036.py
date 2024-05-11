import sys
from collections import defaultdict
input = sys.stdin.readline

def to_36(n):
    if n == 0:
        return '0'
    res = ''
    while n:
        n, r = divmod(n, 36)
        res += '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[r]
    return res[::-1]

N = int(input())
n_list = [input().strip() for _ in range(N)]
K = int(input())

counter = defaultdict(int)
for i in n_list:
    for j in range(len(i)):
        counter[i[(len(i)-1) - j]] += 36 ** j

for i in counter:
    counter[i] *= (35 - int(i, 36))

counter = sorted(counter.items(), key=lambda x: -x[1])

for i in counter[:K]:
    for j in range(len(n_list)):
        n_list[j] = n_list[j].replace(i[0], 'Z')
s = 0
for i in n_list:
    s += int(i, 36)

print(to_36(s))