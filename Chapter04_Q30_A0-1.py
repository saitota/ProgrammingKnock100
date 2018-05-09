from janome.tokenizer import Tokenizer
import janome

import datetime
print('start:' + str(datetime.datetime.now()))

t = Tokenizer()

# WriteのたびにOpen
with open ('./data/neko.txt','r',encoding='utf-8') as file_temp:
    for line in file_temp:
        # 形態素解析して保存
        for token in t.tokenize(line, stream=True):
            with open ('./neko.txt.janome-01','a',encoding='utf-8') as file_janome:
                    file_janome.write(str(token) + '\n')

print('end:' + str(datetime.datetime.now()))

'''
一	名詞,数,*,*,*,*,一,イチ,イチ
吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
猫	名詞,一般,*,*,*,*,猫,ネコ,ネコ
で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
。	記号,句点,*,*,*,*,。,。,。
名前	名詞,一般,*,*,*,*,名前,ナマエ,ナマエ
（以下略）
'''

# start:2018-05-01 14:05:07.333266
# end:2018-05-01 14:07:29.652579
# →  2分22秒