# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_A&lang=ja
while True:
  m, f, r = map(int, input().split())
  if m == -1 and f == -1 and r == -1:
    break
  if m == -1 or f == -1:
    print('F')
    continue
  sum = m + f

  if sum >= 80:
    print('A')
  elif sum >= 65:
    print('B')
  elif sum >= 50:
    print('C')
  elif sum >= 30 and r >= 50:
    print('C')
  elif sum >= 30:
    print('D')
  else:
    print('F')