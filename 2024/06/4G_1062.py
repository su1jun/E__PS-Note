import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:
    print(0)
else:
    K -= 5
    words = [set(input().strip()) for _ in range(N)]
    alpha = set('antic')
    ans = 0

    def dfs(idx, cnt):
        global ans

        if cnt == K:
            temp = 0
            for word in words:
                if word.issubset(alpha):
                    temp += 1
            ans = max(ans, temp)
            return
        
        for i in range(idx, 26):
            if chr(i+ord('a')) not in alpha:
                alpha.add(chr(i+ord('a')))
                dfs(i, cnt+1)
                alpha.remove(chr(i+ord('a')))

    dfs(0, 0)
    print(ans)
