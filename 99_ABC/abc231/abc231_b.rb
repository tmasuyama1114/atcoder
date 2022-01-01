n = gets.to_i
s = []

n.times { |i| s[i] = gets.chomp }

puts s.max_by { |x| s.count(x) }