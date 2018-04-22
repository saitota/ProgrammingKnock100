import argparse
import math

parser = argparse.ArgumentParser(description='hightemp.txt の内容を引数個にファイル分割します')
parser.add_argument('integer', metavar='N', type=int, help='分割する個数を数字で入力')
args = parser.parse_args()

with open ('./data/hightemp.txt','r',encoding='utf-8') as file_in:
    lines = file_in.readlines()
    file_suffix_no = 1
    write_lines = math.ceil( len(lines) / args.integer )
    for integer, line in enumerate(lines):
        with open ('./split_' + str(file_suffix_no) + '.txt', 'a' ,encoding='utf-8') as file_out:
            print(line,end='',file=file_out)
        if ( (integer + 1) % write_lines == 0 ):
            file_suffix_no += 1

