
import re, pyperclip
text = pyperclip.paste()
nigger = re.compile(r'nigger', re.I)
black = re.compile(r'black', re.I)
mo = len(nigger.findall(text)) + len(black.findall(text))
print (mo)
