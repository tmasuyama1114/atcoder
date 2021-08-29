# https://atcoder.jp/contests/abc208/tasks/abc208_b
import math

p = int(input())
rest = p

ans = 0

for i in range(10):
  if rest > math.factorial(10-i):
    pass

  ans += rest // math.factorial(10-i)
  rest = rest % math.factorial(10-i)
  if rest == 0:
    break

print(ans)