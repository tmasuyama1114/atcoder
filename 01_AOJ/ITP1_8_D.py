# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_D&lang=ja
s = input()
p = input()

ring = s + s

if p in ring:
  print("Yes")
else:
  print("No")