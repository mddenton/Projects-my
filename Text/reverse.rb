# Reverse a String - Enter a string and the program
# will reverse it and print it out.

puts ("What would you like to say to me?")
string = gets.chomp
word = ""
chars = string.each_char.to_a
chars.size.times{word << chars.pop}
puts "You say #{string}, I say #{word} "
