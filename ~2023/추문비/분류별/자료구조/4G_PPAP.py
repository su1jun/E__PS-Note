#$ 마지막 체크 문자가 조건문 $#
import sys
input = sys.stdin.readline

S = list(input().rstrip())

stack = []

chk = ["P", "P", "A", "P"]

for i, c in enumerate(S):
    stack.append(c)

    while len(stack) > 3 and stack[-4:] == chk:
        for _ in range(4):
            stack.pop()
        stack.append("P")

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")