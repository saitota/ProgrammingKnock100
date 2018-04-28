import re
# dct_country は Q20 にて取得済みとする
for text in dct_country.get('text').split('\n'):
    match = re.search('\[\[Category.*',text )
    if match != None:
        print(match.group(0))

# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]
