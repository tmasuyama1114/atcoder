# https://atcoder.jp/contests/abc216/tasks/abc216_c
n = int(input())

ans = ""

# 残りボールがちょうど N 個の状態から逆算していく
# 残りボールが2で割り切れるならば B の魔法打つ
# 残りボールが2で割り切れないならば A の魔法を打つ
while (n >= 1):
  if n % 2 == 1:
    ans += "A"
    n -= 1
  else:
    ans += "B"
    n //= 2

# 逆算して魔法順を算出したので、最初からの順番を見るためにはリバース
ans = list(reversed(ans))
ans = ''.join(ans)

print(ans)