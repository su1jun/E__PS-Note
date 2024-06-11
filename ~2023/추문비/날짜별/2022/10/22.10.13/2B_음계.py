import sys
input = sys.stdin.readline

sing = list(map(int, input().split()))
a = True # ascending
b = True # descending

for i in range(8):
    if sing[i] != i+1:
        a = False
    if sing[i] != 8-i: 
        b = False
if a:
    print("ascending")
elif b:
    print("descending")
else:
    print("mixed")