import math
import sys
input = sys.stdin.readline

N = int(input())

prime_number = []
array = [True for _ in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if array[i]:
        j = 2

        while i * j <= N:
            array[i*j] = False
            j += 1

for num in range(2, N + 1):
    if array[num]:
        prime_number.append(num)

cnt = 0
prefix = 0
end = 0

for start in range(len(prime_number)):
    while prefix < N and end < len(prime_number):
        prefix += prime_number[end]
        end += 1

    if prefix == N:
        cnt += 1
    prefix -= prime_number[start]

print(cnt)