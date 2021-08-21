# https://atcoder.jp/contests/abc095/tasks/arc096_a
a, b, c, x, y = map(int, input().split())

##### パターンは3つのみ
# 1. ABピザ を買わない時
s1 = a * x + b * y

# 2. まず AB ピザを最低限買ってから、足りない枚数分を買う
s2 = c * 2 * min(x, y)
if x >= y:
  # 足りない枚数分を買う
  s2 += a * (x-y)
else:
  s2 += b * (y-x)

# 3. AB ピザだけで賄う
s3 = c * 2 * max(x,y)

ans = min(s1, min(s2, s3))
print(ans)