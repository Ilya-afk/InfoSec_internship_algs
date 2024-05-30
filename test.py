import re


YYYY = '[1-9]\\d{3}'
s = input()
result = re.fullmatch(f'^{YYYY}$', s)
if result:
    print('match')
else:
    print('not match')
