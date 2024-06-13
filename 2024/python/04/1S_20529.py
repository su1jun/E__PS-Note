import sys
input = sys.stdin.readline
 
convertor = {
'ISTJ':8, 'ISFJ':10, 'INFJ':14, 'INTJ':12,
'ISTP':9, 'ISFP':11, 'INFP':15, 'INTP':13,
'ESTP':1, 'ESFP':3, 'ENFP':7, 'ENTP':5,
'ESTJ':0, 'ESFJ':2, 'ENFJ':6, 'ENTJ':4,
}

distances = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

for _ in range(int(input())):
    ans = 999999
    N = int(input())
    arr = list(map(str, input().split()))

    if N > 32:
        print(0)
    else:
        arr2 = [convertor[arr[i]] for i in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or i == k:
                        continue
                    temp = distances[arr2[i]^arr2[j]] + distances[arr2[j]^arr2[k]] + distances[arr2[i]^arr2[k]]
                    ans = min(temp, ans)
        print(ans)
