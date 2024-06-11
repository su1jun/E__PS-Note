import sys
import math
input = sys.stdin.readline
 
ans_lst = []
min_num, max_num = map(int, input().split())
validation = [1 for _ in range(min_num, max_num+1)]
 
search_target = int(math.sqrt(max_num))
# max의 값보다 작은 모든 제곱수의 목록을 생성
squr = [v**2 for v in range(2, search_target+1)]
for i in squr:
    # min부터 max까지의 수 중, 해당 제곱수의 최소의 배수를 구함.
    cur_idx = (math.ceil(min_num / i) * i) - min_num
    while cur_idx <= max_num - min_num:
        # 제곱수의 배수인 경우 0으로 대체
        validation[cur_idx] = 0
        # 다음 제곱수의 index를 구함.
        cur_idx += i
 
# 남은 1들의 개수가 제곱 ㄴㄴ수의 개수가 된다.
result = sum(validation)
ans_lst.append(result)
 
for result in ans_lst:
    sys.stdout.write(str(result))