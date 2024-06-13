import sys
input = sys.stdin.readline

N = int(input())
Arr = list(map(int, input().split()))
M = int(input())
Brr = list(map(int, input().split()))


def makeindex(arr):
    result = [[] for _ in range(101)]
	
    for idx, A in enumerate(arr):
        result[A].append(idx) # 원소값이 idx인 원소들의 인덱스를 저장

    for A in range(1, 101):
        result[A].reverse() # 인덱스를 내림차순으로 정렬
        
    return result

indexA = makeindex(Arr)
indexB = makeindex(Brr)

ans = []
curA = -1 # A를 보는 인덱스
curB = -1 # B를 보는 인덱스
for i in range(101, 0, -1):
    while indexA[i] and indexA[i][-1] < curA: indexA[i].pop() # 현재 인덱스보다 작은 인덱스들은 제거
    while indexB[i] and indexB[i][-1] < curB: indexB[i].pop() # ...
    for _ in range(min(len(indexA[i]), len(indexB[i]))):
        curA = indexA[i].pop()
        curB = indexB[i].pop()
        ans.append(i)

print(len(ans))
if len(ans) != 0:
    print(*ans)



