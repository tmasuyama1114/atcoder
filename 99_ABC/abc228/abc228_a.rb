s, t, x = gets.chomp.split.map(&:to_i)

if s > t then
  if x >= s || t > x then
    puts 'Yes'
  else
    puts 'No'
  end
else
  if x >= s && t > x then
    puts 'Yes'
  else
    puts 'No'
  end
end