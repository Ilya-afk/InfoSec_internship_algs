import re


while True:
    s = input()
    result = re.fullmatch(f"^['a-zA-Z0-9._-]+@\\S*\\.\\S*$", s)
    if result:
        print('match')
    else:
        print('not match')
