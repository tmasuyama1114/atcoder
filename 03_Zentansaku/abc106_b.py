# https://atcoder.jp/contests/abc106/tasks/abc106_b
n = int(input())

# 答えの数
ans = 0

for i in range(1, n+1):
  # 偶数は無視
  if i % 2 == 0:
    continue

  # 約数の数を初期化　※必ず約数が 1 つはある
  count = 0

  # i を試しに j で割り、i の約数になりうるかを調べる ※ n の半分まで試せば十分
  for j in range(1, i + 1):
    # j が i の約数であれば count += 1
    if i % j == 0:
      count += 1
  # 約数の数が 8 ならば
  if count == 8:
    ans += 1
print(ans)