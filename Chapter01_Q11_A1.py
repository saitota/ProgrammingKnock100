f = open ('./data/hightemp.txt','r',encoding='utf-8')
text = f.read()
print(text.replace('\t',' '))
# 高知県 江川崎 41 2013-08-12
# 埼玉県 熊谷 40.9 2007-08-16
# (以下略)