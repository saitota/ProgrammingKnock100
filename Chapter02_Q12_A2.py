with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    text = file_temp.read()

lst_col1 = []
lst_col2 = []
for line in text.split('\n'):
    if len(line) > 0:
        lst_col1.append(line.split('\t')[0])
        lst_col2.append(line.split('\t')[1])

with open ('./col1.txt','a',encoding='utf-8') as file_col1:
    print(*lst_col1,sep='\n',file=file_col1)

with open ('./col2.txt','a',encoding='utf-8') as file_col2:
    print(*lst_col2,sep='\n',file=file_col2)