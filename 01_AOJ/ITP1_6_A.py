# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_A&lang=ja
n = int(input())
a = list(map(int, input().split()))

a.reverse()

print(*a)