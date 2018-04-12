file_temp = open ('./data/hightemp.txt','r',encoding='utf-8')
text = file_temp.read()
file_temp.close()
print(text.count('\n'))
# 24
