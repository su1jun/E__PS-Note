<<<<<<< HEAD
#영단어 암기는 괴로워
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
words = defaultdict(int)

for _ in range(N):
    s = input().rstrip()
    
    if len(s) < M:
        continue
    else:
        words[s] += 1

words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

word_lst, cnt = zip(*words)

=======
#영단어 암기는 괴로워
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
words = defaultdict(int)

for _ in range(N):
    s = input().rstrip()
    
    if len(s) < M:
        continue
    else:
        words[s] += 1

words = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

word_lst, cnt = zip(*words)

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print("\n".join(word_lst))