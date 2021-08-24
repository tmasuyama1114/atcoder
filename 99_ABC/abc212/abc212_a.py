# https://atcoder.jp/contests/abc212/tasks/abc212_a
a, b = map(int, input().split())

if 0 < a and b == 0:
  print('Gold')
elif a == 0 and 0 < b:
  print('Silver')
else:
  print('Alloy')