def crypter(texts):
    ret = ''
    for text in texts:
        #a-zなら
        if ord(text) in range(97,123):
            text = chr(219 - ord(text))
        ret += text
    return ret

print(crypter('私は Taro Yamada です'))
# 私は Tzil Yznzwz です
print(crypter(crypter('私は Taro Yamada です')))
# 私は Taro Yamada です
