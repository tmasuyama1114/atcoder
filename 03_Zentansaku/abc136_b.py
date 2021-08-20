# https://atcoder.jp/contests/abc136/tasks/abc136_b

# 文字列として受け取る
n = int(input())

ans = 0

for i in range(1, n+1):
  if len(str(i)) % 2 != 0:
    ans += 1

print(ans)