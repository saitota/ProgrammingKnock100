import re
odai_str = ('I am an NLPer')

def ngram(n,words):
    ansr_lst = []
    for index in range(0, len(words) - n + 1):
        ansr_lst.append(words[index:index + n])
    return ansr_lst

print(ngram(2,re.split(' ', odai_str))) # 配列で渡すと単語n-gram
print(ngram(2,odai_str)) # 文字列で渡すと文字n-gram
