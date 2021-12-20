import re
in_str = "Hi, How are you?"
clean_txt = re.sub(r'\W+', ' ', in_str)
# prints "Hi How are you"
print(clean_txt)