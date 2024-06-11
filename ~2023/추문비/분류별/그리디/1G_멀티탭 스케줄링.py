# 구현 알고리즘, 경우를 잘 나누면서
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
multi_tab = [0] * N
change = max_idx = 0

ans = 0
while arr:
    device = arr[0]
    if device in multi_tab: # 이미 사용 중일때
        arr.remove(device)
        continue

    elif 0 in multi_tab: # 충전 할 빈자리가 있을때
        multi_tab[multi_tab.index(0)] = device
        arr.remove(device)

    else: # 충전 할 빈자리가 없을때
        for tab in multi_tab:
            if tab not in arr: # 나중에 꽂을 필요 없을때
                change = tab
                break

            elif arr.index(tab) > max_idx: # 나중에 꽂을 필요 있을때
                max_idx = arr.index(tab) # 가장 나중의 전기용품 저장
                change = tab

        multi_tab[multi_tab.index(change)] = device
        arr.remove(device)
        max_idx = 0
        ans += 1

print(ans)