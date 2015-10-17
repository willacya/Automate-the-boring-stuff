#! python3

import re, pyperclip

#Get text from clipboard, stipulate search parameters,
#find all words and convert to uppercase.
text = pyperclip.paste()
wordsRegex = re.compile(r"[A-Z']*", re.I|re.VERBOSE)
mo = wordsRegex.findall(text.upper())

#Create dictionary with words found and times they were used.
dic = {}
for key in mo:
    if key not in dic:
        dic.setdefault(key, 1)
    else: 
        dic[key] += 1

#Create list with sublists of words and their times used, from dictionary.
counter = []
for key, value in dic.items():
    counter.append([key, value])

#Sort multilist by wordcount
counter.sort(key=lambda x: (x[1]), reverse=True)

#Print rough total word counter
total = 0
for num in range(len(counter)):
    if counter[num][0] != "" and counter[num][0] != "-":
        total += counter[num][1]
print ("Word Count: " + str(total))
print ("-----------------")
print ("\nMost used words")
print ("-----------------")

#Print beautifully in a three column list
for n in range(1,26): #evades blank spaces being counted
    print (str(n) + ": " + str(counter[n][0]) + " (" + str(counter[n][1]) + ")" )


