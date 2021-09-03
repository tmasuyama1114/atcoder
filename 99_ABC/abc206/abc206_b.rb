# https://atcoder.jp/contests/abc206/submissions/25504919
n = gets.chomp.to_i

i = 0
sum = 0

while sum < n do
  i += 1
  sum += i
end

puts i