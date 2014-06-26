
def letter_count(str)

  counts = {}
  str.downcase.each_codepoint do |char|

    counts[char] = 0 unless counts.include?(char)

    counts[char] += 1

  end

  letter_counts = counts.group_by{ |k, v| v }
  max_char_count = letter_counts.max
  min_char_count = letter_counts.min
  
  max_char = max_char_count.last.map{ |r| r[0] }.min.chr('UTF-8')
  min_char = min_char_count.last.map{ |r| r[0] }.min.chr('UTF-8')

  max_count = counts.fetch(max_char_count.last.map{ |r| r[0] }.min)
  min_count = counts.fetch(min_char_count.last.map{ |r| r[0] }.min)

  print "(#{max_count} '#{max_char}', #{min_count} '#{min_char}' )"

end