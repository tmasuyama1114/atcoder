n, x, y = gets.chomp.split.map(&:to_i)

n.times.each do |i|
  number = i+1 # 応募者の連番
  if number % x ==0 && number % y ==0 then
    puts 'AB'
  elsif number % x ==0 then
    puts 'A'
  elsif number % y ==0 then
    puts 'B'
  else
    puts 'N'
  end
end