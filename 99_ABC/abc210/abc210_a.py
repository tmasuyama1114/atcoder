# https://atcoder.jp/contests/abc210/tasks/abc210_a
n, a, x, y = map(int, input().split())

if n > a:
  print(x * a + y * (n-a))
else:
  print(x * n)