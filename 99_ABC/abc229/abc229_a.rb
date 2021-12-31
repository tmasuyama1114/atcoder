s1 = gets.chomp.chars # 文字列を受け取って１文字ずつ分割して配列に変換
s2 = gets.chomp.chars

if (s1[0] == '.' && s2[1] == '.') || (s1[1] == '.' && s2[0] == '.') then
  puts('No')
else
  puts('Yes')
end