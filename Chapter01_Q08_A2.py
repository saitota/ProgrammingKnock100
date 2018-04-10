def crypter(texts):
    ret = ''
    for text in texts:
        #a-zなら
        if text.islower():
            text = chr(219 - ord(text))
        ret += text
    return ret

print(crypter('私は Taro Yamada です'))
print(crypter(crypter('私は Taro Yamada です')))
