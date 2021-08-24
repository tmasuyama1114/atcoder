# https://atcoder.jp/contests/abc211/tasks/abc211_b
s = []

for i in range(3+1):
  s.append(input())

if ('H' in s) and ('2B' in s) and ('3B' in s) and ('HR' in s):
  print('Yes')
else:
  print('No')