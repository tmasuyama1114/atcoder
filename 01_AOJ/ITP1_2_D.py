# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_D&lang=ja
W, H, x, y, r = map(int, input().split())

"""
x の条件
  r <= x <= W - r
y の条件
  r <= y <= H - r
"""

if ((r <= x) and (x <= W - r)) and ((r <= y) and (y <= H - r)):
  print('Yes')
else:
  print('No')