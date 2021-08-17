# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_D&lang=ja
s = input()
q = int(input())

for i in range(q):
  commands = list(input().split())
  c = commands[0]
  a = int(commands[1])
  b = int(commands[2])

  if c == 'print':
    print(s[a:b+1])

  elif c == 'reverse':
    s = list(s) # 一旦リストにする
    s[a:b+1] = s[a:b+1][::-1] # 指定範囲を反転させたものに置換
    s = ''.join(s) # 文字列に戻す
  else:
    p = commands[3]
    s = list(s) # 一旦リストにする
    s[a:b+1] = list(p)
    s = ''.join(s) # 文字列に戻すs