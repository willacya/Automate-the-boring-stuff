import re

message = "some lame as shit 452-256-6985 aaaand 526-588-9654"

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print (phoneNumRegex.findall(message))

