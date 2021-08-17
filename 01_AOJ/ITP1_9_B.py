# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_B&lang=ja
while True:
  s = input()
  if s == '-':
    break
  m = int(input())

  for i in range(m):
    h = int(input())
    s += s[:h]
    s = s[h:]
  print(s)