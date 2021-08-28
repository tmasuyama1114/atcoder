# https://atcoder.jp/contests/abc209/tasks/abc209_b
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
  if i % 2 != 0:
    a[i] -= 1

if x >= sum(a):
  print('Yes')
else:
  print('No')