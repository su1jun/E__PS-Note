import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = N-1

min_val = abs(arr[left] + arr[right])
ans = [arr[left], arr[right]]

while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val
  
    if abs(sum) < min_val:
        min_val = abs(sum)
        ans = [left_val, right_val]
        if min_val == 0:
          break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(*ans)

'''
import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

ans = float("INF")
ans_left = 0
ans_right = 0

for i in range(n-1):
    current = liquids[i]

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + liquids[mid]

        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        
        if tmp < 0:
            start = mid + 1
        
        else:
            end = mid - 1

print(liquids[ans_left], liquids[ans_right])
'''