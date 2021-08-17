# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_C&lang=ja
n = int(input())

pt_t = 0
pt_h = 0

for i in range(n):
  t, h = input().split()
  if t > h:
    pt_t += 3
  elif t < h:
    pt_h += 3
  else:
    pt_t += 1
    pt_h += 1

print('{} {}'.format(pt_t, pt_h))