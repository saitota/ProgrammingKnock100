odai_str = ('パトカー','タクシー')
ansr_str = ''

for index in range(len(odai_str[0])):
    ansr_str += list(odai_str[0])[index]
    ansr_str += list(odai_str[1])[index]

print(ansr_str)
