# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_A&lang=ja
a, b = map(int, input().split())

print('{} {} {:.5f}'.format(a//b, a%b, a/b))