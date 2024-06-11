import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap= []
    record = defaultdict(int)
    for _ in range(int(input())):
        i, j = input().split()
        if i =='I':
            j = int(j)
            heapq.heappush(min_heap, j)
            heapq.heappush(max_heap, -j)
            record[j] += 1
        elif j =='-1':
            while True:
                if min_heap:
                    t = heapq.heappop(min_heap)
                    if record[t]:
                        record[t] -= 1
                        break
                else:
                    break
        else:
            while True:
                if max_heap:
                    t = heapq.heappop(max_heap)
                    if record[-t]:
                        record[-t] -= 1
                        break
                else:
                    break
    t = record.copy()
    for i in t:
        if record[i] < 1:
            del record[i]
    if record:
        print(max(record), min(record))
    else:
        print('EMPTY')