import sys
input = sys.stdin.readline

#초기 입력
N = int(input()) # 센서의 갯수
K = int(input()) # 집중국의 갯수
arr = sorted(list(map(int, input().split()))) # 센서의 좌표

sbt = []
for i in range(0, N-1):
    sbt.append(arr[i+1] - arr[i])

sbt.sort()

print(sum(sbt[:N-K]))