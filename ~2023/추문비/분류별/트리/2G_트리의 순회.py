import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 분할 정복 방식으로 전위 순회를 찾음
def pre(mid_0, mid_1, post_0, post_1):
    # 재귀 종료 조건 (수렴)
    if(mid_0 > mid_1) or (post_0 > post_1):
        return

    # 후위 순회 결과의 끝이 (서브)트리의 루트임을 이용
    parents = post[post_1]
    print(parents, end=" ")

    # 중위 순회에서 루트의 좌 우로 자식들이 갈라지는 것을 이용하여 left, right를 선언
    left = position[parents] - mid_0
    right = mid_1 - position[parents]

    # left, right로 나눠 분할 정복 방식으로 트리를 추적하여 전위 순회를 찾아냄
    pre(mid_0, mid_0 + left - 1, post_0, post_0 + left - 1) # 쪽 서브트리
    pre(mid_1 - right + 1, mid_1, post_1 - right, post_1 - 1) # 오른쪽 서브트리

N = int(input())
mid = list(map(int, input().split()))
post = list(map(int, input().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
position = [0] * (N+1)
for i in range(N):
    position[mid[i]] = i

# 중위 순회, 후위 순회 모두 0부터 n-1 (전체 범위)값을 주고 전위 순회를 구함
pre(0, N-1, 0, N-1)