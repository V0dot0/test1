import datetime
import re

a = str(datetime.datetime.today())
print(type(a))
time_pattern = r"(?:^\d+\-\d+\-\d+\s)([^\.]+)"
match_name = re.findall(time_pattern, a)
match = ''.join(match_name)
print(match)
print(a)