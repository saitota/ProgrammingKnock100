import re
# dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
match_tmp = ''
match_dct2 = {}
for key,value in match_dct.items():
    match_tmp = re.sub('\'\'+','',value) # 強調を除去
    match_tmp = re.sub('\[\[(.*?)([|\|].*)?\]\]','\\1',match_tmp) # リンクを除去
    match_tmp = re.sub('\{\{lang\|.*?\|(.*?)\}\}','\\1',match_tmp) # {{Lang 要素を除去
    match_tmp = re.sub('<ref.*?( />|</ref>)','',match_tmp) # ref 要素を除去
    match_tmp = re.sub('<br(\s|)/>','',match_tmp) # br 要素を除去
    match_dct2[key] = match_tmp

print (match_dct2)
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': 'United Kingdom of Great Britain and Northern Ireland<ref>英語以外での正式国名:', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': 'ファイル:Royal Coat of Arms of the United Kingdom.svg', '国章リンク': '（イギリスの国章）', '標語': 'Dieu et mon droit（フランス語:神と私の権利）', '国歌': '女王陛下万歳', '位置画像': 'Location_UK_EU_Europe_001.svg',
# （以下略）
