# https://atcoder.jp/contests/abc214/tasks/abc214_c
n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

for i in range(2 * n):
  t[i % n] = min(t[i % n], t[(i-1) % n] + s[(i-1) % n])

for ans in t:
  print(ans)