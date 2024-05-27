from itertools import *
import sys
input = sys.stdin.readline

def solve():
  if len({*N})==K:
    return N
  
  for i in range(1, len(N)+1):
    result = []
    inuse = {*(N0:=N[:-i])}
    notuse = {*map(str, range(10))}-inuse
    k = K-len(inuse)

    if 0<=k<=i:
      for C in combinations(notuse, k):
        C = {*C}
        for H in combinations_with_replacement(inuse|C,i-k):
          willuse = [*H,*C]
          for n in range(int(N[-i])+1,10):
            n = str(n)
            if n in willuse:
              willuse.remove(n)
              result.append(N0+n+"".join(sorted(willuse)))
      if result:
        return min(result)
  return "1"+"0"*(max(len(N)+1,K)-K+1)+"".join(map(str,range(2,K)))

N, K = map(str, input().split())
K = int(K)
print(solve())