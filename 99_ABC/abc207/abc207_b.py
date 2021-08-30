# https://atcoder.jp/contests/abc207/tasks/abc207_b
a, b, c, d = map(int, input().split())

sky = a
red = 0

ans = 0

for i in range(a):
  sky += b
  red += c
  ans += 1
  if sky/red <= d:
    print(ans)
    exit()
print(-1)