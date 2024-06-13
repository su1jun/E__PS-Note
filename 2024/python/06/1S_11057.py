import sys
input = sys.stdin.readline

MOD = 10007

def mod_factorial(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def mod_comb(n, k, mod):
    if k == 0 or k == n: return 1
    numerator = mod_factorial(n, mod)
    denominator = (mod_factorial(k, mod) * mod_factorial(n - k, mod)) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

N = int(input())
result = mod_comb(9 + N, N, MOD)
print(result)