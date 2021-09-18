s1 = input()
s2 = input()
s3 = input()
s = [0, s1, s2, s3]
t = list(map(int, input()))

ans = ''

for i in t:
  ans += s[i]

print(ans)