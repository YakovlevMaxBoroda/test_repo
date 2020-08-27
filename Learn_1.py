dict = {}
with open('Dictionary_Kuznetsov.txt', 'r') as r_txt:
  for line in r_txt:
    key, value = line.split(':')
    key = key.lower()
    dict[key] = str(value[:-1])
print(dict)
with open('ctg_pens_SQL.txt', 'r') as r_txt:
    r_txt = r_txt.read()
newstrings = r_txt
for key in dict.keys():
    if key in r_txt:
        newstrings = newstrings.replace(key, str(dict[key]))
        print(key)
with open('ctg_pens_SQL.txt', 'w') as w_txt:
    w_txt.write(newstrings)
