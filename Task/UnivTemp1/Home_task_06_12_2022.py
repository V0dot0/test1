import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()

title_pattern = r"(?:title-link\">)([^<]*)"
location_pattern = r"(?:location\">\n+\s+)([^\n]+)"
tel_num_pattern = r"(?:Телефон.+\s+<dd class=\"spec__value\">)([^<]+)"
open_time_pattern = r"(?:\">Часы работы.+\s+<dd class=\"spec__value\">)([^<]+)"

match_name = re.findall(title_pattern, response)
match_location = re.findall(location_pattern, response)
match_tel_num = re.findall(tel_num_pattern, response)
match_open_time = re.findall(open_time_pattern, response)

result_list = []
for i in range(len(match_name)-2):
    result_list.append([match_name[i], match_location[i], match_tel_num[i], match_open_time[i]])

print(f"{result_list}")
