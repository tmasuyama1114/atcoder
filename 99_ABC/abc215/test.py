# https://atcoder.jp/contests/abc215/tasks/abc215_d
import math

n, m = map(int, input().split())
a = list(map(int, input().split()))

# math.gcd(a, b)
ans = []


for i in range(n):
  yakusu = [l for l in range(1, i+1) if i % l == 0]
  if len(yakusu) == 1:
    continue

  # i ごとに gcd(a[i], k) == 1 となる k を格納するリスト
  x = []

  for k in range(1, m+1):
    if math.gcd(a[i], k) == 1:
      # print('a[i] = {}, k = {}, gcd = {}'.format(a[i], k, math.gcd(a[i], k)))
      x.append(k)

  if i == 0:
    ans = list(set(x))
  else:
    # 積集合を取る
    ans = set(ans).intersection(set(x))

# set から list へ
ans = list(ans)
ans = sorted(ans)


# 整数の数
print(len(ans))
for e in ans:
  print(e)