#%%
import re

#%%
with open('./hero_data_raw.html', 'r', encoding='utf-8') as f:
    data = f.read()
#%%
ptn = r'{([^{}]*)}'
ptn2 = '\"(\n.*?)a'
ptn3 = "[\u4E00-\u9FFF]+"
res = re.findall(ptn, data)
res = set(res)
with open('./hero_data.json', 'w', encoding='utf-8') as f:
    f.write('{\n')
    for i in res:
        ii = re.sub(ptn2, "\"a", i)
        tmp = re.findall(ptn3, ii)
        ii = "\t\"hero_" + tmp[0] + "\":{" + ii + "},\n"
        print(ii)
        f.write(ii)
    f.write('}')
