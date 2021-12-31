m = gets.to_i
a = []
m.times.each do
  a << gets.to_i
end

n = gets.to_i
b = []
n.times.each do
  b << gets.to_i
end

visited_lives = []
last_visited_live_is_a = false # 最後にいったライブが A であれば true

[*1..31].each do |i|
  if a.include?(i) && b.include?(i) then
    last_visited_live_is_a ? visited_lives[i-1] = 'B' : visited_lives[i-1] = 'A'
    last_visited_live_is_a = !last_visited_live_is_a
  elsif a.include?(i) then
    visited_lives[i-1] = 'A'
  elsif b.include?(i) then
    visited_lives[i-1] = 'B'
  else
    visited_lives[i-1] = 'x'
  end
  puts visited_lives[i-1]
end

# 出力
visited_lives.each do |visited_live|
  # puts visited_live
end