import sys
input = sys.stdin.readline

while True:
    stk = ['love']
    a = input()
    if a == '.\n':
        break

    for j in a:
        if j == '(':
            stk.append(j)
        elif j == '[':
            stk.append(j)

        elif j == ')':
            if stk[-1] == '(':
                stk.pop()
            else: 
                print("no")
                break
        elif j == ']':
            if stk[-1] == '[':
                stk.pop()
            else: 
                print("no")
                break

    else:
        if stk[-1] == 'love':
            print("yes")
        else:
            print("no")