import sys
input = sys.stdin.readline

#초기 입력
N, K = map(int, input().split()) # N : 원생의 수, K : 조의 갯수
arr = list(map(int, input().split()))

tmp = []
for i in range(1, N):
    tmp.append(arr[i] - arr[i-1])
tmp.sort()
print(sum(tmp[:N-K]))
