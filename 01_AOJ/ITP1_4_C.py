# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_C&lang=ja

while True:
  a, op, b = input().split()
  a = int(a)
  b = int(b)
  if op == '+':
    print(a + b)
  elif op == '-':
    print(a - b)
  elif op == '*':
    print(a * b)
  elif op == '/':
    print(a // b)
  else:
    break