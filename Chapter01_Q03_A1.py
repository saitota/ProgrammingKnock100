import re
odai_str = ('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
ansr_lst = []

for value in re.split(' ', odai_str):
    ansr_lst.append(len(re.sub(r'\W','',value)))

print(ansr_lst)
