import sys
import heapq
input = sys.stdin.readline

#초기 입력
N = int(input()) # 수업 갯수
table = [list(map(int, input().split())) for _ in range(N)]
table.sort()

heap = []
heapq.heappush(heap, table[0][1])

for i in range(1, N):
    if table[i][0] < heap[0]:
        heapq.heappush(heap, table[i][1])
    else:
        heapq.heapreplace(heap, table[i][1])
print(len(heap))
