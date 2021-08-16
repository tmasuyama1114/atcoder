# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_A&lang=ja
while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0:
    break
  for i in range(H):
    l = ''
    for j in range(W):
      l += '#'
    print(l)
  print('')