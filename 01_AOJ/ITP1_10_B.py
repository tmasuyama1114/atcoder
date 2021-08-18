# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_B&lang=ja
from math import sin, cos, pi, sqrt

a, b, c = map(float, input().split())

# a が底辺

# 面積
S = a * (b * sin(pi*c/180)) / 2
print(S)

# 周の長さ
L = a + b + sqrt(a**2 + b**2 - 2 * a * b *cos(pi*c/180))
print(L)

# 高さ h
h = b * sin(pi*c/180)
print(h)