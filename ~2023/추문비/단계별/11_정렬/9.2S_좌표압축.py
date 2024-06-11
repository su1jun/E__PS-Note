import sys
N = int(sys.stdin.readline())
dic = {}

p = list(map(int, sys.stdin.readline().split()))
p_s = list(set(p.copy()))
p_s.sort()

cnt = 0

for i in p_s:
    dic[i] = cnt
    cnt += 1

for i in p:
    print(dic[i], end=" ")

###
# n = int(input())
# arr = list(map(int, input().split()))
# sorted_arr = sorted(list(set(arr)))

# n_dict = {}
# for i, n in enumerate(sorted_arr):
#   if n in n_dict:
#     continue
#   else:
#     n_dict[n] = i
  

# answer = ''
# for i in arr:
#   answer += str(n_dict[i]) + ' '

# print(answer[:-1])

###
# N = int(input())
# coords = list(map(int,input().split()))

# rank = list(set(coords))
# rank.sort()

# index = {}
# for i in range(len(rank)):
#     index[rank[i]] = i

# print(*[index[i] for i in coords])