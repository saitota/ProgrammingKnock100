import gzip,json

with gzip.open('./data/jawiki-country.json.gz',mode='rt',encoding='utf=8') as gz_temp:
     countrys_json = gz_temp.read()

country_dict = []
for country_json in countrys_json.split('\n'):
    if len(country_json) > 1: # 空行がエラーになるため
      country_dict.append(json.loads(country_json))

for country in country_dict:
    if country.get('title') == 'イギリス':
        print(country.get('text'))
# {{redirect|UK}}
# {{基礎情報 国
# |略名 = イギリス
# |日本語国名 = グレートブリテン及び北アイルランド連合王国
# |公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
# *{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>
# *{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>
# （以下略）