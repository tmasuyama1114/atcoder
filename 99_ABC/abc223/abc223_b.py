s = list(input())

s_min = "".join(s)
s_max = "".join(s)

for i in range(len(s)):
  s.append(s[0])
  del s[0]

  if s_min > "".join(s):
    s_min = "".join(s)
  if s_max < "".join(s):
    s_max = "".join(s)

print(s_min)
print(s_max)