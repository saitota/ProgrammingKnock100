odai_str = ('paraparaparadise','paragraph')

def ngram(n,words):
    ansr_lst = []
    for index in range(0, len(words) - n + 1):
        ansr_lst.append(words[index:index + n])
    return ansr_lst

lst_x = ngram(2,odai_str[0])
lst_y = ngram(2,odai_str[1])
set_x = set(lst_x)
set_y = set(lst_y)

print(set_x.union(set_y))
print(set_x.intersection(set_y))
print(set_x.difference(set_y))

