# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D&lang=ja
a, b, c = map(int, input().split())

ans = 0

for i in range(a, b+1):
  if c % i == 0:
    ans += 1
print(ans)