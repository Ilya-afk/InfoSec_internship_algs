import re


YYYY = '[1-9]\\d{3}'
MM = '(0\\d|1[0-2])'
DD = '([0-2]\\d|3[0-1])'
hh = '([0-1]\\d|2[0-3])'
mm = '([0-5]\\d)'
ss = '([0-5]\\d)'

s = input()
date = re.fullmatch(f'((^{YYYY}-{MM}$|^{YYYY}{MM}{DD}$)|^{YYYY}-{MM}-{DD}$)', s)
time = re.fullmatch(f'(((^{hh}{mm}$|^{hh}:{mm}$)|^{hh}{mm}{ss}$)|^{hh}:{mm}:{ss}$)', s)
time_with_zone = re.fullmatch(f'(^{hh}{mm}{ss}[+-]{hh}{mm}?$|^{hh}:{mm}:{ss}[+-]{hh}$)', s)
datetime = re.fullmatch(f'(^{YYYY}{MM}{DD}T{hh}{mm}{ss}$|'
                        f'^{YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}$)', s)
datetime_with_zone = re.fullmatch(f'((^{YYYY}{MM}{DD}T{hh}{mm}{ss}[+-]{hh}{mm}?$|'
                                  f'^{YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}[+-]{hh}$)|'
                                  f'^{YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}[+-]{hh}:{mm}$)', s)
if date:
    print('match date')
elif time:
    print('match time')
elif time_with_zone:
    print('match time with zone')
elif datetime:
    print('match datetime')
elif datetime_with_zone:
    print('match datetime with zone')
else:
    print('not match')
