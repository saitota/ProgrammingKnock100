import random

def mixer(text):
    ret = ''
    for words in text.split(' '):
        if len(words) > 4:
            shufflelist = list(words[1:-1:])
            random.shuffle(shufflelist) # なかシャッフル
            shufflelist.insert(0,words[0:1:]) # 1文字目 挿入
            shufflelist.append(words[-1::]) # 末尾文字 追加
            words = ''.join(shufflelist)
        ret += words + ' '
    return ret

print(mixer("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
# I cnul'dot bvileee that I cluod aaltlcuy usdnnrtead what I was radieng : the pmhoeaennl power of the human mind .
