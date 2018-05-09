from janome.tokenizer import Tokenizer
import janome

import datetime
print('start:' + str(datetime.datetime.now()))

t = Tokenizer()

# リスト内包表記
with open ('./data/neko.txt','r',encoding='utf-8') as file_temp , open ('./neko.txt.janome','a',encoding='utf-8') as file_janome:
    [
        [
            file_janome.write(str(x) + '\n')
            for x in t.tokenize(y, stream=True)
        ]
        for y in file_temp
    ]

print('end:' + str(datetime.datetime.now()))

# start:2018-05-01 14:41:10.212988
# end:2018-05-01 14:41:50.549268
# → 0分40秒
