import sys
N, K = list(map(int,sys.stdin.readline().split()))

def power(a,b):
    if b==0:
        return 1
    else:
        if b % 2:
            return (power(a,b//2)**2*a) % p
        else:
            return (power(a,b//2)**2) % p

p = 1000000007
fct = [1 for _ in range(N+1)]
for i in range(1,N+1):
    fct[i] = (fct[i-1]*i) % p
t1 = fct[N]
t2 = (fct[K]*fct[N-K])%p

print((t1 * power(t2,p-2))%p )
