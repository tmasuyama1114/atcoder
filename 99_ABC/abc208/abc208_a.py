# https://atcoder.jp/contests/abc208/tasks/abc208_a
a, b = map(int, input().split())

if a <= b <= a * 6:
  print('Yes')
else:
  print('No')