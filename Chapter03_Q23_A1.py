import re
# dct_country は Q20 にて取得済みとする
match = re.findall('(==+)(.*?)==+',dct_country.get('text'),re.MULTILINE)
devnull = [print(v[1] + ' is Level ' +  str(v[0].count('='))) for v in match]
# 国名 is Level 2
# 歴史 is Level 2
# 地理 is Level 2
# 気候 is Level 3
# 政治 is Level 2
# 外交と軍事 is Level 2
# (以下略)
