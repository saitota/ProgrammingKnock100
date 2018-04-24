with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    text = file_temp.read()

lst_col1 = []
lst_answer = []
for line in text.split('\n'):
    lst_col1.append(line.split('\t')[0])

lst_col1.sort()
lst_answer = set(lst_col1) #dict?

for value in lst_answer:
    print(value)