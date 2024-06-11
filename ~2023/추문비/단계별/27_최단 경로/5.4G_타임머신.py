import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    weight[start] = 0
    for i in range(V):
        for j in range(E):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            edge_cost = graph[j][2]
            # 거쳐갈때가 더 짧을때
            if weight[cur_node] != INF and weight[next_node] > weight[cur_node] + edge_cost:
                weight[next_node] = weight[cur_node] + edge_cost
                # v번째에서도 값이 갱신되면 음수 순환의 존재
                if i == V - 1:
                    return True

    return False

V, E = map(int, input().split())
graph = []
weight = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

ans = bellman_ford(1)
if ans:
    print("-1")
else:
    # 1번 노드를 제외하고 다른 모든 노드로 갈때
    for i in range(2, V + 1):
        if weight[i] == INF:
            print("-1")
        else:
            print(weight[i])