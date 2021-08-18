# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_A&lang=ja
import math

x1, y1, x2, y2 = map(float, input().split())

d_square = ((y2 - y1)**2 + (x2 - x1)**2)
d = math.sqrt(d_square)
print(d)