import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

print(A+B-C)
temp = int(str(A) + str(B))
print(temp-C)