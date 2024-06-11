import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M, R = map(int, input().split()) # N : 정점 갯수, M : 간선 갯수, R = 시작 정점
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1) # 방문처리
ans = ["0"] * (N+1) # 방문순서
order = 1 # 순서계산
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(n): # n : 방문 정점, m : 방문 순서
    global order
    visited[n] = 1
    ans[n] = str(order)
    order += 1
    for i in sorted(graph[n]):
        if not visited[i]:
            dfs(i)
    
dfs(R)
print("\n".join(ans[1:]))

# from sys import stdin, setrecursionlimit

# setrecursionlimit(10000)
# def get_graph(N, M) -> list:
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, stdin.readline().split())
#         graph[a].append(b)
#         graph[b].append(a)
    
#     for i in range(len(graph)):
#         graph[i].sort(reverse=True)
#     return graph

# def main():
#     N, M, R = map(int, stdin.readline().split())
#     graph = get_graph(N, M) # if node numbers are discrete or character 
#                             using dictionary would be better.
#     res = [0] * N 
#     def dfs_recursion(start):
#         visited.add(start)
#         global cnt
#         res[start-1] = cnt
#         cnt += 1
#         for x in graph[start]:
#             if x not in visited:
#                 dfs(x)
#     def dfs_while(start):
#         stack = [start]
#         visited = set() 
#         cnt = 1
#         while stack:
#             tmp = stack.pop()
#             if tmp in visited:
#                 continue
#             visited.add(tmp)
#             res[tmp-1] = cnt
#             cnt += 1
#             for adj_node in graph[tmp]:
#                 if adj_node not in visited:
#                     stack.append(adj_node)

    
#     dfs_recursion(R)
#     dfs_while(R)


#     print('\n'.join(map(str, res)))

# if __name__ == '__main__':
#     cnt = 1
#     main()
