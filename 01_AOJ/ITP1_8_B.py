# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_B&lang=ja

while True:
  s = input()
  if s == '0':
    break
  nums = list(map(int, s))
  print(sum(nums))
