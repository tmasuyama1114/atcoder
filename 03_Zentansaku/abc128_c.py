# https://atcoder.jp/contests/abc128/tasks/abc128_c
n, m = map(int, input().split()) # ex: n = 2, m = 2

k = [0] * m # ex: [0, 0]
s = [0] * m # ex: [0, 0]

for i in range(m):
  ks = list(map(int, input().split()))
  k[i] = ks[0]
  s[i] = ks[1::]
# ex: k = [2, 1]
# ex: s = [[1,2], [2]]

p = list(map(int, input().split())) # ex: [0, 1]

# 電球が消えているものがあれば 0
judge = 0

# 組み合わせの数
ans = 0

for bit in range(1 << n): # ex: bit = 10
  for i in range(m): # ex: i = 0 番目の電球について
    count = 0 # i番目の電球が繋がっているスイッチのうち on になっている数
    for j in s[i]: # ex: i = 0 番目の電球が繋がっているスイッチを一つずつチェック
      if bit & (1 << j-1): # bit に j 番目のフラグが立っているか => yes = s[i][j] は点灯
        count += 1
      print('bit = {}, i = {}, j = {}'.format(bit, i, j-1))
    if count % 2 == p[i]:
      judge = 1
    else:
      judge = 0
  if judge == 1:
    ans += 1

print(ans)