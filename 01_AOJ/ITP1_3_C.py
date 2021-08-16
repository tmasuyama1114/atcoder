# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_C&lang=ja

while True:
  a = list(map(int, input().split()))
  a.sort()
  if a == [0, 0]:
    break
  print('{} {}'.format(a[0], a[1]))