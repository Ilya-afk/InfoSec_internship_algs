import re


s = input()
result = re.findall("[:;]-*[(){}\\]\\[]+", s)
print(len(result))
