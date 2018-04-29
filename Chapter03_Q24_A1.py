import re
# dct_country は Q20 にて取得済みとする
match = re.findall('File:(.*?)\|',dct_country.get('text'),re.MULTILINE)
devnull = [print(v) for v in match]
# Battle of Waterloo 1815.PNG
# The British Empire.png
# Uk topo en.jpg
# BenNevis2005.jpg
# (以下略)
