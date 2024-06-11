import sys
input = sys.stdin.readline
 
# 초기 입력
S = list(input().rstrip()) # S : 판별 문자열
C = list(input().rstrip()) # C : 폭발 문자열

ans = []

lC = len(C) # C의 길이

for i in range(len(S)):
    la = len(ans)+1 # ans의 길이

    if S[i] != C[-1]:
        ans.append(S[i])
    else:
        ans.append(S[i])
        if la >= lC:
            if ans[-lC:] == C:
                for _ in range(lC):
                    ans.pop()
                print(f"조건 완료 : idx : {i} ans : {ans}")

if ans:
    print("".join(ans))
else:
    print("FRULA")