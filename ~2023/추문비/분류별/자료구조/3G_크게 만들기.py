import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().rsplit()) # N:자릿수, K:지울 갯수
num = list(map(int, input().rstrip()))
heap = []
lst = [(0, -1)]

st = 0
end = K+1

while end <= N:
    for i in range(st, end):
        heapq.heappush(heap, (-num[i], i))

    tmp = heapq.heappop(heap)
    while lst[-1][1] > tmp[1]:
        tmp = heapq.heappop(heap)
    lst.append(tmp)
    K -= lst[-1][1] - (lst[-2][1] + 1)

    st = end
    end = (lst[-1][1]+1) + (K+1)

# 출력 양식
ans = []
for i in range(1, len(lst)):
    ans.append(-lst[i][0])
ans += num[st:-2]
print(*ans, sep='')


N, K = map(int, input().split())
num = list(input())

ans = []
cnt = K
for i in num:
    while ans and cnt > 0 and ans[-1] < i:
        del ans[-1]
        cnt -= 1
    ans.append(i)
    
print(''.join(ans[:N-K]))