# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_D&lang=ja
n, m, l = map(int, input().split())

a = [[0]*m for line in range(n)]
b = [[0]*l for line in range(m)]
c = [[0]*l for line in range(n)]

# a を生成
for i in range(n):
  line_a = list(map(int, input().split()))
  for j in range(m):
    a[i][j] = line_a[j]

# b を生成
for i in range(m):
  line_b = list(map(int, input().split()))
  for j in range(l):
    b[i][j] = line_b[j]

# c を生成
for i in range(n):
  for j in range(l):
    for k in range(m):
      c[i][j] += a[i][k] * b[k][j]
  print(' '.join(map(str, c[i])))