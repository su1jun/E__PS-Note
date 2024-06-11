import sys
input = sys.stdin.readline

String = input().rstrip() # 문자열
L = len(String)
A = String.count("a")

ans = []
String2 = String + String
for i in range(2*L-A):
    ans.append(String2[i:i+A].count("b"))
print(min(ans))
