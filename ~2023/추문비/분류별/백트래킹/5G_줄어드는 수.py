import sys
input = sys.stdin.readline

def dfs():
    if len(arr) > 0:
        result.add(int("".join(map(str, arr))))

    for i in range(0, 10):
        if len(arr) == 0 or arr[-1] > i:  # 마지막 값이 더 큰 경우
            arr.append(i)
            dfs()
            arr.pop()

arr = []
result = set()

N = int(input())

try:
    dfs()
    result = list(result)
    result.sort()
    print(result[N - 1])
except:
    print(-1)