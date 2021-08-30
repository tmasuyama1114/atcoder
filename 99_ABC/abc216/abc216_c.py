# https://atcoder.jp/contests/abc216/tasks/abc216_c
n = int(input())

boll = 0

# 最短で n を超える試行回数: m
boll += 1  # ここで１回分消費
m = 1
while True:
  boll *= 2
  m += 1
  if boll >= n:
    break

print(m)
