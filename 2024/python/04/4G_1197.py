import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# kruskal algorithm
# def find(x):
#     if parent[x] == x: return x
#     else:
#         parent[x] = find(parent[x])
#         return parent[x]

# def union(a, b):
#     ar, br = find(a), find(b)

#     if ar != br:
#         if ar < br: parent[br] = ar
#         else:
#             parent[ar] = br
#         return True
#     return False

# V, E = map(int, input().split())
# parent = [i for i in range(V+1)]
# anwser = 0
# arr = [list(map(int, input().split())) for _ in range(E)]

# arr.sort(key=lambda x : x[2])

# for a, b, c in arr:
#     if union(a, b):
#         anwser += c

# print(anwser)

# prim algorithm
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
heap = [[0, 1]]
anwser = 0
cnt = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

while heap:
    if cnt == V: break

    cost, node = heapq.heappop(heap)
    if visited[node]: continue

    visited[node] = True
    anwser += cost
    cnt += 1
    for temp in graph[node]:
        heapq.heappush(heap, temp)

print(anwser)