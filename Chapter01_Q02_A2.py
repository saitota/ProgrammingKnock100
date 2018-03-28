odai_str = ('パトカー','タクシー')
ansr_str = ''

for item1, item2 in zip(odai_str[0],odai_str[1]):
    ansr_str += item1 + item2

print(ansr_str)
