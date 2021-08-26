# https://atcoder.jp/contests/abc210/tasks/abc210_b
n = int(input())
s = list(input())

for i in range(n):
  if s[i] == '1':
    if i % 2 == 0:
      print("Takahashi")
    else:
      print("Aoki")
    break
