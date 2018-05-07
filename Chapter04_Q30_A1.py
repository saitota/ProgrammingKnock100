
with open ('./neko.txt.janome','r',encoding='utf-8') as file_temp:
    #for line in file_temp:
    #    print(line)
    text = file_temp.readlines()

for line in text:
    print(line)

