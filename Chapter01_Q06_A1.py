odai_str = ('paraparaparadise','paragraph')

def ngram(n,words):
    ansr_lst = []
    for index in range(0, len(words) - n + 1):
        ansr_lst.append(words[index:index + n])
    return ansr_lst

def union_set(x,y):
    tmp_lst = x + y
    tmp_lst2 = []
    for val in tmp_lst:
        if tmp_lst2.count(val) == 0:
            tmp_lst2.append(val)
    return tmp_lst2

def prod_set(x,y):
    tmp_lst = []
    for val_x in x:
        for val_y in y:
            if (val_x == val_y) and (val_y not in tmp_lst):
               tmp_lst.append(val_y)
    return tmp_lst

def diff_set(x,y):
    tmp_lst = []
    for val_x in x:
        if (val_x not in y) and (val_x not in tmp_lst):
            tmp_lst.append(val_x)
    return tmp_lst

def check_se(x):
    return 'se' in (x)

lst_x = ngram(2,odai_str[0])
lst_y = ngram(2,odai_str[1])

print(union_set(lst_x,lst_y))
# ['pa', 'ar', 'ra', 'ap', 'ad', 'di', 'is', 'se', 'ag', 'gr', 'ph']
print(prod_set(lst_x,lst_y))
# ['pa', 'ar', 'ra', 'ap']
print(diff_set(lst_x,lst_y))
# ['ad', 'di', 'is', 'se']
print(check_se(lst_x))
# True
print(check_se(lst_y))
# False
