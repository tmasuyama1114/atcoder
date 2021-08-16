# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B&lang=ja
n = int(input())

# マークごとにカードが存在する数字を格納するリスト
spead = []
heart = []
club = []
diamond = []

for i in range(n):
  mark, num = input().split()
  num = int(num)

  if mark == 'S':
    spead.append(num)
  elif mark == 'H':
    heart.append(num)
  elif mark == 'C':
    club.append(num)
  else:
    diamond.append(num)

# スペードについてチェック
for j in range(1, 13 + 1):
  if spead.count(j) == 0:
    print('S {}'.format(j))

# ハートについてチェック
for j in range(1, 13 + 1):
  if heart.count(j) == 0:
    print('H {}'.format(j))


# クラブについてチェック
for j in range(1, 13 + 1):
  if club.count(j) == 0:
    print('C {}'.format(j))

# ダイヤについてチェック
for j in range(1, 13 + 1):
  if diamond.count(j) == 0:
    print('D {}'.format(j))
