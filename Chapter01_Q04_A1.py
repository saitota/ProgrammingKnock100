import re
odai_str = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
ansr_dct = {}

tmp_lst = []
for value in re.split(' ', odai_str):
    tmp_lst.append(re.sub(r'\W','',value))

for index,value in enumerate(tmp_lst):
    if (index + 1) in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        ansr_dct.update( { tmp_lst[index][0:1]: index + 1 } )
    else:
        ansr_dct.update( { tmp_lst[index][0:2]: index + 1 } )

print(ansr_dct)
# {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}