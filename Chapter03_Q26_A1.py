import re
# dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
match_dct2 = {}
for key,value in match_dct.items():
     match_dct2[key] = re.sub('\'\'+','',value)

print (match_dct2)
# (中略)
# '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更'
# (後略)
