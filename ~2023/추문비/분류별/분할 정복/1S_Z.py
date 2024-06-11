import sys
input = sys.stdin.readline

# 초기값
N, r, c = map(int, input().split())

##1 2
##
##3 4

def f(n, x, y):
    if n > 1:
        k = 2 ** (n-1)
        if x < k:
            if y < k: # 제 1사분면
                print(f"n : {n} // k : {k} // x : {x} // y : {y} // 1 : {0}")
                return f(n-1, x, y)

            else: # 제 2사분면
                print(f"n : {n} // k : {k} // x : {x} // y : {y} // 2 : {k ** 2}")
                return f(n-1, x, y-k) + (k ** 2)

        else:
            if y < k: # 제 3사분면
                print(f"n : {n} // k : {k} // x : {x} // y : {y} // 3 : {(k ** 2) * 2}")
                return f(n-1, x-k, y) + (k ** 2) * 2

            else: # 제 4사분면
                print(f"n : {n} // k : {k} // x : {x} // y : {y} // 4 : {(k ** 2) * 3}")
                return f(n-1, x-k, y-k) + (k ** 2) * 3

    else:
        if x == 0:
            if y == 0:
                return 0
            else:
                return 1
        else:
            if y == 0:
                return 2
            else:
                return 3

print(f(N, r, c))