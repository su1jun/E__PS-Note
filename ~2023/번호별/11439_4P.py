<<<<<<< HEAD
input = __import__('sys').stdin.readline

n, k, m = map(int, input().split())
nk = n-k

primes = [2, 3]
for prime_candidate in range(5, n+1, 2):
    flag = False
    for prime in primes:
        if prime**2 > prime_candidate:
            break
        if prime_candidate % prime == 0:
            flag = True
            break
    
    if not flag:
        primes.append(prime_candidate)

n_dec, nk_dec, k_dec = dict(), dict(), dict()
def calc_dec(num: int, dec: dict):
    for prime in primes:
        prime_pow = prime
        while prime_pow <= num:
            dec[prime] = dec.get(prime, 0) + num // prime_pow
            prime_pow *= prime
calc_dec(n, n_dec)
calc_dec(nk, nk_dec)
calc_dec(k, k_dec)
        
binom_dec = dict()
for key, value in n_dec.items():
    exp = n_dec[key] - nk_dec.get(key, 0) - k_dec.get(key, 0)
    if exp == 0:
        continue
    else:
        binom_dec[key] = exp

def pow(n, k, m):
    if k == 1:
        return n
    pow_half = pow(n, k//2, m)
    if k % 2 == 0:
        return (pow_half ** 2) % m
    else:
        return (pow_half ** 2 * n) % m

result = 1
for key, value in binom_dec.items():
    result *= pow(key, value, m)
    result %= m

=======
input = __import__('sys').stdin.readline

n, k, m = map(int, input().split())
nk = n-k

primes = [2, 3]
for prime_candidate in range(5, n+1, 2):
    flag = False
    for prime in primes:
        if prime**2 > prime_candidate:
            break
        if prime_candidate % prime == 0:
            flag = True
            break
    
    if not flag:
        primes.append(prime_candidate)

n_dec, nk_dec, k_dec = dict(), dict(), dict()
def calc_dec(num: int, dec: dict):
    for prime in primes:
        prime_pow = prime
        while prime_pow <= num:
            dec[prime] = dec.get(prime, 0) + num // prime_pow
            prime_pow *= prime
calc_dec(n, n_dec)
calc_dec(nk, nk_dec)
calc_dec(k, k_dec)
        
binom_dec = dict()
for key, value in n_dec.items():
    exp = n_dec[key] - nk_dec.get(key, 0) - k_dec.get(key, 0)
    if exp == 0:
        continue
    else:
        binom_dec[key] = exp

def pow(n, k, m):
    if k == 1:
        return n
    pow_half = pow(n, k//2, m)
    if k % 2 == 0:
        return (pow_half ** 2) % m
    else:
        return (pow_half ** 2 * n) % m

result = 1
for key, value in binom_dec.items():
    result *= pow(key, value, m)
    result %= m

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
print(result)