# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_C&lang=ja
a, b = map(int, input().split())
area = a * b
rectangle = (a + b) * 2
print('{} {}'.format(area, rectangle))