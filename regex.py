import re
# Alt + R to search for regex 
# \d for digits, \D for non-digits  in a file 
pattern = "[a-zA-z0-9]+@[a-zA-Z]+\.(com|eu|net)"

user_input = input()

if(re.search(pattern, user_input)):
 print("Valid email")
else:
 print("Invalid email")