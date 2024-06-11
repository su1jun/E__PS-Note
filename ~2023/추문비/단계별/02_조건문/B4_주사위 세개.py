A, B, C =map(int, input().split(" "))
reward = 0

if A == B:
    if A == C:
        reward = 10000 + A * 1000
    else:
        reward = 1000 + A * 100
else:
    if A == C:
        reward = 1000 + A * 100
    elif B == C:
        reward = 1000 + B * 100
    else:
        reward = max(A, B, C) * 100
print(reward)