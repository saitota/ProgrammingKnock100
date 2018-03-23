odai_str = ('stressed')
ansr_str = ''

list_str = list(odai_str)
for index in range(len(list_str)):
    rev_index = len(list_str) - index -1
    ansr_str += list_str[rev_index]

print(ansr_str)