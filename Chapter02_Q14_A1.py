import sys

arg = int(sys.argv[1])
text = ''
with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    for i in range(arg):
        text += file_temp.readline()

print(text)

