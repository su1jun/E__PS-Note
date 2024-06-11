import sys
input = sys.stdin.readline

N = int(input()) # 유전자 갯수
dna = list(map(str, input().split()))
set1 = []
set2 = []
for i in dna:
    if i not in set1:
        set1.append(i)
    elif i not in set2:
        set2.append(i)

dna = set1 + set2
ans = []

l = len(dna)
for i in range(l):
    for j in range(l):
        if i != j:
            print(f"{i}, {j} / {dna[i][0]}+{dna[j][1]}")
            ans.append(sorted(dna[i][0]+dna[j][1])[1])

ans = list(set(ans))
print(len(ans))
print(*sorted(ans))

print("a"<"b")