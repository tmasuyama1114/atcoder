# https://atcoder.jp/contests/abc120/tasks/abc120_b
a, b, k = map(int, input().split())

# common divisor (公約数) を格納するリスト
cd = []

# a の約数を d_a に追加
for i in range(1, 100 + 1):
  if (a % i == 0) and (b % i == 0):
    cd.append(i)

# 並び替える必要はない
print(cd[-k])