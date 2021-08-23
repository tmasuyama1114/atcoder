# https://atcoder.jp/contests/abc182/tasks/abc182_c
n = input() # ex: n = 321

# 桁数
l = len(n) # ex: l = 3

# 消す桁数の初期値 (Max)
ans = l # 全桁を消すことはないので本来ならばありえない (ルール違反なのでこのときは -1 を出力させる)

for bit in range(1 << l): # 考えうるすべての bit に対して全探索　ex:bit = 101
  res = ""
  for i in range(l): # ex: i = 0
    if bit & (1 << i): # bit に i 番目のフラグが立っているかどうか  # 101 に 1 番目のフラグが立っているか -> yes
      res += n[i] # ex: res = '3'
  # ex: 全部まわしたら bit = 101 に対して res = '31' となっている
  if res == "": # bit と and を取る桁が一つもなければ次の bit へ (いるか？)
    continue
  if int(res) % 3 == 0: # bit との and を取って一部桁を消した後の数が 3 の倍数かどうかを調べる
    ans = min(ans, l - len(res)) # l=len(n) と len(res) の差し引き = 消した桁数

print(ans if ans != l else -1)