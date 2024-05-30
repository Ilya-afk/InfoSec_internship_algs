import re


s = input()
octet = '(((\\d|[1-9]\\d)|1\\d\\d)|(2[0-4]\\d|25[0-5]))'
result = re.fullmatch(f'^{octet}[.]{octet}[.]{octet}[.]{octet}(/((\\d|[1-2]\\d)|3[0-2]))?$', s)
if result:
    print('match')
else:
    print('not match')
