import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return db[20][20][20]

    else:
        return db[a][b][c]

N = 21

db = [[[1 for _ in range(N)] for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, N):
        for k in range(1, N):
            if i < j and j < k:
                db[i][j][k] = db[i][j][k-1] + db[i][j-1][k-1] - db[i][j-1][k]

            else:
                db[i][j][k] = db[i-1][j][k] + db[i-1][j-1][k] + db[i-1][j][k-1] - db[i-1][j-1][k-1]
            

while True:
    q = sys.stdin.readline()
    nums = list(map(int, q.split()))
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")