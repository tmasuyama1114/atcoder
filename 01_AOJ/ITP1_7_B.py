# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
while True:
  n, x = map(int, input().split())
  if n == 0 and x == 0:
    break

  # 組み合わせの数
  ans = 0

  for a in range(1, n-1):
    for b in range(a+1, n):
      for c in range(b+1, n+1):
        if a + b + c == x:
          ans +=1
  print(ans)