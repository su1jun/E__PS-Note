import sys
input = sys.stdin.readline

def binary_search(LisArr, num):
    left = -1
    right = len(LisArr)

    while left + 1 < right:
        mid = (left + right) // 2
        if num > LisArr[mid]:
            left = mid
        else:
            right = mid
    return right

LisArr = [-1e9-1]
LisIdx = [(-1e9-1, 0)]

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()

while arr:
    num = arr.pop()

    if num > LisArr[-1]:
        LisIdx.append((num, len(LisArr)))
        LisArr.append(num)
    else:
        idx = binary_search(LisArr, num)
        LisIdx.append((num, idx))
        LisArr[idx] = num

ans_len = len(LisArr)-1
print(ans_len)
ans = []

while LisIdx and ans_len:
    num, idx = LisIdx.pop()
    if idx == ans_len:
        ans.append(num)
        ans_len -= 1
print(*ans[::-1])