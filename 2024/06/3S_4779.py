def rec(n):
  if n == 0: return '-'
  return rec(n-1) + ' ' * 3 ** (n-1) + rec(n-1)

while True:
  try:
    print(rec(int(input())))
  except:
    break