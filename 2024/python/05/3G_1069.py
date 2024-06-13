import sys
input = sys.stdin.readline

X, Y, D, T = map(int, input().split())

dist = (X**2 + Y**2)**0.5

if dist < D:
    ans = min(dist, T+D-dist, 2*T)
else:
    jump = dist//D
    ans = min(dist, jump*T + dist-jump*D, (jump+1)*T)
    
print(f"{ans:0.10f}")
