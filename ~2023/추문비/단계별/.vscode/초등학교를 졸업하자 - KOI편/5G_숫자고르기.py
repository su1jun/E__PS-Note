import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def dfs(start, i):
    print(f"start: {start}, i: {i}, st: {st}")
    if arr[i] == start:
        print(f"success: {len(st) + 1}")
        return len(st) + 1
    elif arr[i] in st:
        return 0
    else:
        st.add(arr[i])
        dfs(start, arr[i]-1)

h = 0
anw = []
print("arr", arr)
print("anw", anw)
for i in range(n):
    st = set()
    print(f"dfs(i + 1, i): {dfs(i + 1, i)}")
    if dfs(i + 1, i) > 0:
        anw.append([i + 1, dfs(i + 1, i)])
print(anw)

