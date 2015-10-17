import re, pyperclip, pprint

text = pyperclip.paste()
wordsRegex = re.compile(r"[a-zA-Z'-]*", re.I)
mo = wordsRegex.findall(text.upper())
dic = {}
for i in mo:
    if i not in dic:
        dic.setdefault(i, 1)
    else: 
        dic[i] += 1
counter = []
for key, value in dic.items():
    counter.append([key, value])


counter.sort(key=lambda x: (x[1]), reverse=True)


for n in range(25):
    print (str(counter[n][1]) + " "  + str(counter[n][0]))
