
def letter_count(str)

  counts = {}
  str.downcase.each_codepoint do |char|

    counts[char] = 0 unless counts.include?(char)

    counts[char] += 1

  end

  max_char = counts.group_by{ |k, v| v }.max.last.map{ |r| r[0] }.min.chr('UTF-8')
  min_char = counts.group_by{ |k, v| v }.min.last.map{ |r| r[0] }.min.chr('UTF-8')

  max_count = counts.fetch(counts.group_by{ |k, v| v }.max.last.map{ |r| r[0] }.min)
  min_count = counts.fetch(counts.group_by{ |k, v| v }.min.last.map{ |r| r[0] }.min)

  print "(#{max_count} '#{max_char}', #{min_count} '#{min_char}' )"

end