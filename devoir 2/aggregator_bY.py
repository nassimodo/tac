from os import listdir
from os.path import isfile, join

print('Hello World!')
#ignored = set(["conseil communal", "conseil général"])

YEAR = 1855

txt_path = './bulletins'

txts = [f for f in listdir(txt_path) if isfile(join(txt_path, f)) and str(YEAR) in f]
content_list = []
for txt in txts:
    with open(f'{txt_path}/{txt}', encoding='utf-8') as f:
        content_list.append(f.read())


with open(f'tmp/{YEAR}.txt', 'w') as f:
    f.write(' '.join(content_list))

#print(content_list)

