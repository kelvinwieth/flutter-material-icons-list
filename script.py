import requests
import re
import json

url = 'https://raw.githubusercontent.com/flutter/flutter/master/packages/flutter/lib/src/material/icons.dart'

# Line example: static const IconData ten_mp_sharp = IconData(0xe701, fontFamily: 'MaterialIcons');
response = requests.get(url)
body = response.content.decode()
lines = body.split(sep = '\n')

lines_with_icon = [line for line in lines if line.startswith('  static const IconData ') and line.endswith('fontFamily: \'MaterialIcons\');')]

result = {}

for line in lines_with_icon:
	namePattern = r'static\s+const\s+IconData\s+(\w+)\s*='
	codePattern = r'IconData\((0x[0-9a-fA-F]+)'
	name = re.search(namePattern, line).group(1)
	code = re.search(codePattern, line).group(1)
	result[name] = code

with open('icons.json', 'w', encoding='utf-8') as file:
	json.dump(result, file, ensure_ascii=False, indent=4)
