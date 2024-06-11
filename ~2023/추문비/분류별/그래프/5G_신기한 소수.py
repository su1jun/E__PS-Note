import math, sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def is_prime(number):
    number = int(number)
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

def dfs(number):
    if len(number) == N:
        print(number)
        return
    for n in tail_numbers:
        if is_prime(number+n):
            dfs(number+n)

N = int(input())
head_numbers = ['2', '3', '5', '7']
tail_numbers = ['1', '3', '7', '9']

for n in head_numbers:
    dfs(n)