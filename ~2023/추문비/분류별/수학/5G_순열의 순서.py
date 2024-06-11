import sys
import math
input = sys.stdin.readline

N = int(input()) # 순열
arr = list(map(int, input().rsplit())) # 배열

tmp = [i for i in range(1, N+1)]

if arr[0] == 1:
    ans = []
    k = arr[1]-1
    for i in range(1, N):
        f = math.factorial(N-i)
        idx = k//f

        ans.append(tmp[idx])
        del tmp[idx]
        k %= f

    ans.append(tmp[0])
    print(*ans)

else:
    ans = 0
    for i in range(1, N):
        ans += tmp.index(arr[i]) * math.factorial(N-i)
        tmp.remove(arr[i])
    print(ans+1)