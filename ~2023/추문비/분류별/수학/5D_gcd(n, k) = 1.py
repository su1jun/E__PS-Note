import sys
input = sys.stdin.readline

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y // 2
        x = (x*x) % p
    return res

def miller_rabin(n, a):
    r = 0
    d = n-1
    while d % 2 == 0:
        r += 1
        d = d//2

    x = power(a, d, n)
    if x == 1 or x == n-1:
        return True

    for _ in range(r-1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False

def is_prime(n):
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for a in alist:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def g(x,n):
    return ((x*x) + 1) % n

def pola(n,x):
    p = x
    if is_prime(n):
        return n
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:
            x = g(x,n)
            y = g(g(y,n),n)
            d = gcd(abs(x-y),n)
        if d == n:
            return pola(n,p+1)
        else:
            if is_prime(d):
                return d
            else:
                return pola(d,2)

n = int(input())
ori_n = n
ans = []

while n != 1:
    k = pola(n,2)
    ans.append(int(k))
    n = n // k

from itertools import combinations

check_sum = ori_n
ans = list(set(ans))
for i in range(1,len(ans)+1):
    for t in combinations(ans,i):
        k = 1
        for p in t:
            k *= p
        if i % 2 == 1:
            check_sum -= (ori_n // k)
        else:
            check_sum += (ori_n // k)

if ori_n == 1:
    print(1)
else:
    print(check_sum)