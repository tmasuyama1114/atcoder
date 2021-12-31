n = gets.to_i
a = gets.split(' ').map(&:to_i)
a = a.sort # 少ない順に並び替え
candy_got = [0] * n # i 番目の子どもがもらったキャンディの数を格納する配列

n.times.each do |i|
  candy_got[i] = a[i] + a[-(i+1)]
end
puts candy_got.max - candy_got.min