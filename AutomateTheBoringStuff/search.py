# Pytohon3

import pyperclip, re, pprint, operator
wordDic = {}
wordRegex = re.compile(r'''[a-zA-Z'"-]*''')
text = pyperclip.paste()
findRegex = wordRegex.findall(text)
print (findRegex)
for word in findRegex:
    if word not in wordDic:
        wordDic[word] = 1
    else:
        wordDic[word] += 1
pprint.pprint(wordDic)
