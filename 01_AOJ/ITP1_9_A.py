# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_A&lang=ja
import itertools

W = input()

# 空リストを生成
t = []

while True:
  T = input()
  if T == 'END_OF_TEXT':
    break
  t.append(T.lower().split())
  # for element in T:
  # t.append(T.lower())

# 二次元リストを一次元リストに変換
t = list(itertools.chain.from_iterable(t))

print(t.count(W))