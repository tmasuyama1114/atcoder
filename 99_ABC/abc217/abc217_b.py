# https://atcoder.jp/contests/abc217/tasks/abc217_b
s = []

for i in range(3):
  s.append(input())

if 'ABC' not in s:
  print('ABC')
elif 'ARC' not in s:
  print('ARC')
elif 'AGC' not in s:
  print('AGC')
else:
  print('AHC')