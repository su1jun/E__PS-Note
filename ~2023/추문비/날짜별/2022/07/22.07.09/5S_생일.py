import sys

n = int(sys.stdin.readline())
mans = dict()

for _ in range(n):
    a = list(map(str, sys.stdin.readline().split()))
    mans[a[0]]=int(a[3])*365+int(a[2])*30.5+int(a[1])

print(max(mans, key= lambda x : mans[x]))
print(min(mans, key= lambda x : mans[x]))
