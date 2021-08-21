# https://atcoder.jp/contests/abc057/tasks/abc057_c
import math
n = int(input())

# ループ上限
m = int(math.sqrt(n)) + 1

# F を格納するリスト
f = []
for a in range(1, m):
  # b が整数になり得るかどうかを判定
  if n % a == 0:
    b = int(n / a)
    # print('a = {}   b = {}'.format(a, b))
  else:
    continue
  # a と b で桁が大きい方
  digit_larger = max(len(str(a)), len(str(b)))
  f.append(digit_larger)

print(min(f))