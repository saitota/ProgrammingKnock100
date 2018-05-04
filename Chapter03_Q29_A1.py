import re
import urllib.request
# dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)

image_name = re.sub('\[\[ファイル:(.*?)\|.*\]\]','\\1',match_dct['国章画像']) # ファイル名を抽出
param = {
    'format': 'json',
    'action': 'query',
    'titles': 'File:Royal%20Coat%20of%20Arms%20of%20the%20United%20Kingdom.svg',
    'prop': 'imageinfo',
    'iiprop': 'url'
}
query = '&'.join("%s=%s" % (k, v) for k, v in param.items())
url = 'http://en.wikipedia.org/w/api.php?%s'  % (query)
request = urllib.request.urlopen(url)
jsonData = request.read().decode('utf-8')
data = json.loads(jsonData)
print(data.get('query').get('pages').get('-1').get('imageinfo')[0].get('url'))
# 'https://upload.wikimedia.org/wikipedia/commons/9/98/Royal_Coat_of_Arms_of_the_United_Kingdom.svg'
