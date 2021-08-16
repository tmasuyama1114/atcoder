# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_C&lang=ja
r, c = map(int, input().split())

table = [[0]*(c+1) for i in range(r+1)]

for i in range(r):
  line = list(map(int, input().split()))
  for j in range(c):
    table[i][j] = line[j]

for i in range(r):
  for j in range(c):
    # 表の右端を計算
    table[i][c] += table[i][j]
  # 表の右下を計算 (全合計)
  table[r][c] += table[i][c]

for j in range(c):
  for i in range(r):
    # 表の下を計算
    table[r][j] += table[i][j]

for i in range(r+1):

  for j in range(c+1):
    # 最初のみ空白を入れない
    if j == 0:
      print('{}'.format(table[i][j]), end="")
    else:
      print(' {}'.format(table[i][j]), end="")
  print()