# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C&lang=ja
n = int(input())

# 各棟の情報を生成 (初期値はすべて 0)
table = [[[0]*10 for i in range(3)] for j in range(4)]

for add in range(n):
  b, f, r, v = map(int, input().split())

  # b棟 の f階 の r番目の部屋 に v 人を入居させる処理
  table[b-1][f-1][r-1] += v

for i in range(4):
  if i != 0:
    print('#'*20)
  for j in range(3):
    for k in table[i][j]:
      print(' {}'.format(k), end="")
    print()
