<<<<<<< HEAD
# 냅색 문제
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))

leftWei = weights[:N//2]
rightWei = weights[N//2:]
leftSum = []
rightSum = []

def bruteForce(weis, sums, l, w):
    if l >= len(weis):
        sums.append(w)
        return
    bruteForce(weis, sums, l + 1, w)
    bruteForce(weis, sums, l + 1, w + weis[l])

def binarySearch(start, end, arr, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

bruteForce(leftWei, leftSum, 0, 0)
bruteForce(rightWei, rightSum, 0, 0)
rightSum.sort()

cnt = 0
l = len(rightSum)
for i in leftSum:
    if C < i:
        continue
    cnt += binarySearch(0, l, rightSum, C-i)
=======
# 냅색 문제
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))

leftWei = weights[:N//2]
rightWei = weights[N//2:]
leftSum = []
rightSum = []

def bruteForce(weis, sums, l, w):
    if l >= len(weis):
        sums.append(w)
        return
    bruteForce(weis, sums, l + 1, w)
    bruteForce(weis, sums, l + 1, w + weis[l])

def binarySearch(start, end, arr, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

bruteForce(leftWei, leftSum, 0, 0)
bruteForce(rightWei, rightSum, 0, 0)
rightSum.sort()

cnt = 0
l = len(rightSum)
for i in leftSum:
    if C < i:
        continue
    cnt += binarySearch(0, l, rightSum, C-i)
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(cnt)