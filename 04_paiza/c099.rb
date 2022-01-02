n, d = gets.split(' ').map(&:to_i)
overlapping_sizes = []
(n-1).times { overlapping_sizes << gets.to_i }

overlapping_sizes_sum = overlapping_sizes.inject(:+)

puts d * (n * d - overlapping_sizes_sum)