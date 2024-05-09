import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
pq = []
parents = [i for i in range(N)]

for i in range(N):
    row = list(input().rstrip())
    for j in range(i+1, N):
        if row[j] == 'Y': heapq.heappush(pq, [i, j]) # i < j인 간선만 입력

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
    
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

if len(pq) < M: print(-1)
# 간선의 개수가 m개보다 적을 때에는 정답 X
else:
    answer = [0 for _ in range(N)]
    # 각 노드의 연결 횟수를 저장할 리스트
    # 크루스칼 알고리즘을 통해 MST 만들기
    edge_num = 0
    pq2 = []
    while pq: # pq에 남은 간선이 없을 때까지
        node1, node2 = heapq.heappop(pq)
        if union(node1, node2): # 두 노드가 연결되어 있지 않다면
            answer[node1] += 1
            answer[node2] += 1
            edge_num += 1
        else: # 이미 연결되어 있다면
            heapq.heappush(pq2, [node1, node2])
    if edge_num != N-1: print(-1) # MST가 아닌 경우
    else:
        for _ in range(M-edge_num): # 남은 간선을 연결
            node1, node2 = heapq.heappop(pq2)
            answer[node1] += 1
            answer[node2] += 1
        print(*answer)