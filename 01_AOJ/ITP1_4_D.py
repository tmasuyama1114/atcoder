# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_D&lang=ja
n = int(input())
a = list(map(int, input().split()))

min = min(a)
max = max(a)
sum = sum(a)

print('{} {} {}'.format(min, max, sum))