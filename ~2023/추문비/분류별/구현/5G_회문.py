# 조건을 간단히, 회문일때 검사 한번, 유사회문일때 검사 한번
import sys
input = sys.stdin.readline

def ispalindrome(string, left, right):
    if string == string[::-1]:
        return 0
    else:
        while left < right:
            if string[left] != string[right]:
                if ispseudo(string, left+1, right) or ispseudo(string, left, right-1):
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

def ispseudo(string, left, right):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

T = int(input())
for _ in range(T):
    S = input().rstrip()
    L, R = 0, len(S)-1
    ans = ispalindrome(S, L, R)
    print(ans)