# https://atcoder.jp/contests/abc150/tasks/abc150_b
n = int(input())
s = input()

count = 0

for i in range(n-2):
  if s[i:i+3] == 'ABC':
    count += 1

print(count)