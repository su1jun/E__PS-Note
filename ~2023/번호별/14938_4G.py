<<<<<<< HEAD
input = __import__('sys').stdin.readline
import heapq
INF = int(1e9)

def dikkstra(n):
    heap = []
    dis = [INF] * (N+1)

    heapq.heappush(heap, [0, n])
    dis[n] = 0

    while heap:
        now_dis, now_loc = heapq.heappop(heap)

        for next_dis, next_loc in arr[now_loc]:
            if next_dis + now_dis < dis[next_loc]:
                dis[next_loc] = next_dis + now_dis
                heapq.heappush(heap, [next_dis + now_dis, next_loc])
    
    return dis

N, M, R = map(int, input().split())

area_item = list(map(int, input().split()))
area_item.insert(0, 0)

arr = [[] for _ in range(N+1)]

for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start].append([dist, end])
    arr[end].append([dist, start])

max_val = int(-1e9)

for i in range(1, N+1):
    temp_sum = 0
    result = dikkstra(i)

    for j in range(1, N+1):
        if result[j] <= M:
            temp_sum += area_item[j]
    
    if max_val < temp_sum: max_val = temp_sum

=======
input = __import__('sys').stdin.readline
import heapq
INF = int(1e9)

def dikkstra(n):
    heap = []
    dis = [INF] * (N+1)

    heapq.heappush(heap, [0, n])
    dis[n] = 0

    while heap:
        now_dis, now_loc = heapq.heappop(heap)

        for next_dis, next_loc in arr[now_loc]:
            if next_dis + now_dis < dis[next_loc]:
                dis[next_loc] = next_dis + now_dis
                heapq.heappush(heap, [next_dis + now_dis, next_loc])
    
    return dis

N, M, R = map(int, input().split())

area_item = list(map(int, input().split()))
area_item.insert(0, 0)

arr = [[] for _ in range(N+1)]

for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start].append([dist, end])
    arr[end].append([dist, start])

max_val = int(-1e9)

for i in range(1, N+1):
    temp_sum = 0
    result = dikkstra(i)

    for j in range(1, N+1):
        if result[j] <= M:
            temp_sum += area_item[j]
    
    if max_val < temp_sum: max_val = temp_sum

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(max_val)