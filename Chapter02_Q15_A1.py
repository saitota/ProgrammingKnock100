import argparse

parser = argparse.ArgumentParser(description='hightemp.txt の内容を末尾から指定行表示します')
parser.add_argument('integer', metavar='N', type=int, help='表示する行数を数字で入力')
args = parser.parse_args()

with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    lines = file_temp.readlines()
    text = ''
    for linenumber in range(len(lines)-args.integer,len(lines)):
        text += lines[linenumber]

print(text)

