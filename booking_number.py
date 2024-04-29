import re


s = input()
result = re.fullmatch('^[A-Z][0-8][A-Z]{3}[0-35-9][/-][a-z]{2}$', s)
if result:
    print('match')
else:
    print('not match')
