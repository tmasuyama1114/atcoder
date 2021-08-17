# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_C&lang=ja
import sys
import string
# 入力
# for l in sys.stdin.read():
#   s += l

# # 小文字化
# s = s.lower()

# # 一文字ずつリスト化
# s = list(s)

s=[x.lower() for x in sys.stdin.read().split()]

# アルファベット一覧
alphabets = list(string.ascii_lowercase)
# [chr(ord('a') + i) for i in range(26)] # 他の書き方
# [chr(i) for i in range(97, 97+26)] # 他の書き方

for alphabet in alphabets:
  ans = s.count(alphabet)
  print('{} : {}'.format(alphabet, ans))