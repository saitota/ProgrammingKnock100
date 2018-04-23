with open ('./data/hightemp.txt','r',encoding='utf-8') as file_temp:
    lines = file_temp.readlines()

lines2 = []
lines3 = [] 
lines4 = []
for line in lines:
    lines2.append(line.split('\t'))

for  line2 in lines2:
    lines3.append([float(line2[2])] + line2 )

lines4 = sorted(lines3, reverse=True)
for line4 in lines4:
    del line4[0]  # 1列目を消す
    print ('\t'.join(line4), end='')
# 高知県  江川崎  41      2013-08-12
# 岐阜県  多治見  40.9    2007-08-16
# 埼玉県  熊谷    40.9    2007-08-16
# (中略)
# 埼玉県  鳩山    39.9    1997-07-05
# 千葉県  茂原    39.9    2013-08-11
