import re


s = input()
result = re.sub('\\s+', '*', s)
print(result)
