# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja
import math

while True:
  n = int(input())
  if n == 0:
    break
  s = list(map(float, input().split()))

  # average m
  m = sum(s) / n

  a2 = 0

  for element in s:
    a2 += (element - m) ** 2

  a2 = math.sqrt(a2 / n)

  print(a2)