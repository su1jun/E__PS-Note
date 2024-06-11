import sys
import itertools
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
K = int(input())

def kmp(pattern, all_string):
    l = len(pattern)
    table = [0] * l
    idx = 0
    for i in range(1, l):
        while idx > 0 and pattern[idx] != pattern[i]:
            idx = table[idx-1]
        if pattern[idx] == pattern[i]:
            idx += 1
            table[i] = idx
    
    cnt = -1
    idx = 0
    for i in range(len(all_string)):
        while idx > 0 and pattern[idx] != all_string[i]:
            idx = table[idx-1]
        if pattern[idx] == all_string[i]:
            idx += 1
            if idx == l:
                cnt += 1
                idx = table[idx-1]
    
    return cnt == K
ans = 0
permutations = list(itertools.permutations(words, N))
for perm in permutations:
    a = ''.join(list(perm))
    ans += kmp(a, a+a)
print(ans)