import itemgetter
with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    text = file_temp.read()

lst_col1 = []
lst_col2 = []
for line in text.split('\n'):
    lst_col1.append(line.split('\t')[0])

lst_col1.sort()
for value in set(lst_col1):
    if value != '': #空行処理
        lst_col2.append([lst_col1.count(value)]  + [value])

lst_col2.sort(key=lambda x:x[0]) # [0]順に昇順ソート
lst_col2.refverse() # ひっくり返して降順

for value in lst_col2:
    print(value)
