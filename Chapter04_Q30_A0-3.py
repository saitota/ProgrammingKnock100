from janome.tokenizer import Tokenizer
import janome

import datetime
print('start:' + str(datetime.datetime.now()))

t = Tokenizer()

# 一部リスト内包表記
with open ('./data/neko.txt','r',encoding='utf-8') as file_temp , open ('./neko.txt.janome','a',encoding='utf-8') as file_janome:
    for line in file_temp:
        # 形態素解析して保存
        [file_janome.write(str(x) + '\n') for x in t.tokenize(line, stream=True)]
            

print('end:' + str(datetime.datetime.now()))

# start:2018-05-01 14:40:19.827371
# end:2018-05-01 14:41:00.948506
# → 0分41秒
