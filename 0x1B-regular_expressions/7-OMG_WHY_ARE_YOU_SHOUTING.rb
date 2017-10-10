#!/usr/bin/env ruby
# substitues all the non caps letters to "", so only the 
# cap letters are printed out
puts(ARGV[0].gsub(/[^A-Z]/, ""))
