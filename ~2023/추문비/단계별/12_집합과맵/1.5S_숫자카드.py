import sys
N = int(sys.stdin.readline())
nums1 = list(map(int, sys.stdin.readline().split()))
nums1.sort()

M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

def bin_sch(arr, target, s, e):
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return None

ans = ''
for i in range(M):
    if bin_sch(nums1, nums2[i], 0, N - 1) is not None:
        ans += '1 '
    else:
        ans += '0 '
print(ans.rsplit())