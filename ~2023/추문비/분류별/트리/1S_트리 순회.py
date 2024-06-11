import sys
input = sys.stdin.readline

tree = {}
for n in range(int(input())):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])

def mid(root):
    if root != '.':
        mid(tree[root][0])
        print(root, end='')
        mid(tree[root][1])

def post(root):
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root, end='')

pre('A')
print()
mid('A')
print()
post('A')