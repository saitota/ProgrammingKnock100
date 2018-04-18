with open ('./col1.txt','r',encoding='utf-8') as col1_temp:
    text_col1 = col1_temp.read()
with open ('./col2.txt','r',encoding='utf-8') as col2_temp:
    text_col2 = col2_temp.read()

col1and2 = ''
for col1,col2 in zip(text_col1.split('\n'),text_col2.split('\n')):
    col1and2 += col1 + '\t' + col2 + '\n'

with open ('./col1and2.txt','a',encoding='utf-8') as file_col1and2:
    print(col1and2,file=file_col1and2)

# 高知県	江川崎
# 埼玉県	熊谷
# (以下略)