def cipher(texts):
    ret = ''
    for text in texts:
        #a-zなら
        if text.islower():
            text = chr(219 - ord(text))
        ret += text
    return ret

print(cipher('私は Taro Yamada です'))
print(cipher(cipher('私は Taro Yamada です')))
