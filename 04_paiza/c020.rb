m, p, q = gets.split.map(&:to_f)

rest = m # 初期値
rest -= m * p / 100
rest = rest - rest * q / 100
puts rest