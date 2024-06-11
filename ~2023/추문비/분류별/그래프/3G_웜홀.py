import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    weight = [INF] * (N+1) # 거리 초기화
    weight[start] = 0
    for i in range(N):
        for j in range(2*M+W):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            edge_cost = graph[j][2]
            # 거쳐갈때가 더 짧을때
            if weight[next_node] > weight[cur_node] + edge_cost:
                weight[next_node] = weight[cur_node] + edge_cost
                # n번째에서도 값이 갱신되면 음수 순환의 존재
                if i == N - 1:
                    return True

    return False

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    graph = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    # 음의 싸이클의 판별
    key = bellman_ford(1)
    if key:
        print("YES")
    else:
        print("NO")