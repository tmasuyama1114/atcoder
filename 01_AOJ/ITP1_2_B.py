# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_B&lang=ja
a, b, c = map(int, input().split())

if (a < b) and (b < c):
  print('Yes')
else:
  print('No')