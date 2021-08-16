# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_C&lang=ja
while True:
  H, W = map(int, input().split())
  if H == 0 and W == 0:
    break
  for i in range(H):
    l = ''
    if i % 2 == 0:
      for j in range(W):
        if j % 2 == 0:
          l += '#'
        else:
          l += '.'
      print(l)
    else:
      if i % 2 == 1:
        for j in range(W):
          if j % 2 == 0:
            l += '.'
          else:
            l += '#'
      print(l)

  print('')