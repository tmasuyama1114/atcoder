# https://atcoder.jp/contests/abc217/tasks/abc217_c
n = int(input())
p = list(map(int, input().split()))

q = [' ']*n

for i in range(1,n+1):
  q[p[i-1]-1] = str(i)

print(' '.join(q))