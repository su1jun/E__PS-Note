import sys
input = sys.stdin.readline

def ticketPick(count):

    total = 0
    w = 0
    for i in range(len(count)-1):
        w += count[i]
        useTicket = ticket[i][0] * w
        useICcard = ticket[i][1] * w + ticket[i][2]
        total += min( useTicket, useICcard)
    return total

def cityCount(path):
    for i in range(len(path) -1 ):
        a = min(path[i],path[i+1])
        b = max(path[i],path[i+1])
        count[a] +=1
        count[b] -=1

N, M = input().split()
N, M = int(N),int(M)
path = [int(k)-1 for k in input().split()]
ticket = []
count = [0] * (N)
for i in range(N-1):
    ticket.append([int(k) for k in input().split()])

cityCount(path)
print(ticketPick(count))