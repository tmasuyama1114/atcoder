# https://atcoder.jp/contests/abc122/tasks/abc122_b
s = input()

# ACGT 文字列を @ に置き換え
s = s.replace('A', '@').replace('C', '@').replace('G', '@').replace('T', '@')

ans = 0
max_ans = 0

for i in range(len(s)):
  if s[i] == '@':
    ans += 1
    if ans > max_ans:
      max_ans = ans
  else:
    ans = 0

print(max_ans)