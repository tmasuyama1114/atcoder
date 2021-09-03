# https://atcoder.jp/contests/abc206/tasks/abc206_a
n = gets.to_i

x = (n * 1.08).floor # 小数切り捨て
if x < 206 then
  puts "Yay!"
elsif x == 206 then
  puts "so-so"
else
  puts ":("
end