import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

for _ in range(T):
    N = int(input()) # 전화번호 갯수
    arr = [input().rstrip() for _ in range(N)] # 전화번호 부
    arr.sort() # 정렬

    for i in range(N-1):
        l = len(arr[i])
        if arr[i] == arr[i+1][:l]: # 접두사끼리만 비교
            print('NO')
            break
    else:
        print('YES')