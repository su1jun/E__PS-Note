<<<<<<< HEAD
# 다각형의 면적
input = __import__('sys').stdin.readline

lst1 = []
lst2 = []
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    lst1.append(x)
    lst2.append(y)
lst1.append(lst1[0])
lst2.append(lst2[0])

a, b = 0, 0
for i in range(N):
    a += lst1[i] * lst2[i+1]
    b += lst2[i] * lst1[i+1]

print(abs(round((a-b)/2, 1)))
=======
# 다각형의 면적
input = __import__('sys').stdin.readline

lst1 = []
lst2 = []
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    lst1.append(x)
    lst2.append(y)
lst1.append(lst1[0])
lst2.append(lst2[0])

a, b = 0, 0
for i in range(N):
    a += lst1[i] * lst2[i+1]
    b += lst2[i] * lst1[i+1]

print(abs(round((a-b)/2, 1)))
>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
