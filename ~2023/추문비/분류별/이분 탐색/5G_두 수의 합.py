import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()

    low = 200000000
    for j in range(N):
        left = j+1
        right = N-1
        while(left <= right):
            mid = (left + right) // 2
            sum = num[j] + num[mid]
            if(sum > K):
                right = mid-1
            else:
                left = mid+1
            if(abs(K-sum) < low):
                cnt = 1
                low = abs(K-sum)
            elif(abs(K-sum) == low):
                cnt+=1
    print(cnt)