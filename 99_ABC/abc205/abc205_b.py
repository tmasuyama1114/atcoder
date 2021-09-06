# https://atcoder.jp/contests/abc205/submissions/me
n = int(input())
a = list(map(int, input().split()))

list_n = []
for i in range(n):
  list_n.append(i+1)

a.sort()

if a == list_n:
  print('Yes')
else:
  print('No')