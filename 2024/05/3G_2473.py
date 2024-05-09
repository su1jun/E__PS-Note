import sys
input = sys.stdin.readline

N = int(input())
Arr = list(map(int, input().split()))
Arr.sort()

def two_pointer():
    best_Val = sys.maxsize
    best_Val_lst = []

    for i in range(N-2):
        start, end = i+1, N-1
        while start < end:
            mixture = Arr[start] + Arr[end] + Arr[i]

            if abs(mixture) < best_Val:
                best_Val = abs(mixture)
                best_Val_lst = [Arr[start], Arr[end], Arr[i]]

            if mixture > 0: # 특성값 합 낮추기
                end -= 1 
            elif mixture < 0:# 특성값 합 높이기
                start += 1
            else:
                return best_Val_lst
    else:
        return best_Val_lst

ans = two_pointer()
ans.sort() 
print(*ans)