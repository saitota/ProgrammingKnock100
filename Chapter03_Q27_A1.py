import re
# dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
match_tmp = ''
match_tmp2 = ''
match_dct2 = {}
for key,value in match_dct.items():
    match_tmp = re.sub('\'\'+','',value) # 強調を除去
    match_tmp = re.sub('\[\[(.*?)([|\|].*)?\]\]','\\1',match_tmp) # リンクを除去
    match_dct2[key] = match_tmp

print (match_dct2)
# (中略)
# '確立形態2': 'グレートブリテン王国建国<br />（連合法 (1707年)）',
# (後略)
