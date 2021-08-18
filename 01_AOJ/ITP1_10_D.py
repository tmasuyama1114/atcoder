# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

z = [0]*n

def calc(p):
  D = 0

  if p != 1000000:
    for i in range(n):
      z[i] = abs(x[i] - y[i]) ** p
    D = (sum(z)) ** (1/p)
  else:
    for i in range(n):
      z[i] = abs(x[i] - y[i])
    D = max(z)
  print(D)

for i in range (1, 3+1):
  calc(i)
calc(1000000)