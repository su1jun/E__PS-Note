import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(N)]

    scores.sort()
    max_score = scores[0][1]
    ans = 0

    for i in range(1, N):
        if max_score >= scores[i][1]:
            ans += 1

        elif scores[i][0] <= max_score < scores[i][1]:
            max_score = scores[i][1]
    
    print(ans)