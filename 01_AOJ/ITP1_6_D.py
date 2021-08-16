# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_D&lang=ja
n, m = map(int, input().split())

# 空行列/ベクトルを生成
a = [[0]*m for i in range(n)]
b = [0]*m
c = [0]*n

# 入力
for i in range(n):
  a[i] = list(map(int, input().split()))

for j in range(m):
  b[j] = int(input())

# 計算
for j in range(n):
  for k in range(m):
    c[j] += a[j][k] * b[k]
  print(c[j])