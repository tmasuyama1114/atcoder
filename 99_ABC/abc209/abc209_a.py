# https://atcoder.jp/contests/abc209/tasks/abc209_a
a, b = map(int, input().split())

if b >= a:
  print(b-a+1)
else:
  print(0)