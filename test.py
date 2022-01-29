# -*- coding: utf-8 -*-
import re

text_ = "{'_id': {'N': '1'}, 'tr_langues_id': {'N': '9'}, 'tr_composant_phrases_id': {'BOOL': True}, 'composition': {'BOOL': false}}"

regex_ = "'N': '\\d'"
regex_ = r"\d"
pattern = re.compile(regex_)

"""
print(bool(pattern.match(text_)))

if pattern.match(text_):
    print("pattern yes")
else:
    print("pattern no")
"""

m = re.search(r"'N': '[0-9]+'", text_, re.DOTALL)


#print(m.group(0))
#print(m.groups())
if bool(m) is True:
    print("re yes")
    print(m.groups())
else:
    print("re no")

print(re.sub(r"'N': '([0-9]+)'", r"'N': \1", str(text_)))

print(re.sub(r"'BOOL': (true|True)", r"'BOOL': 1", str(text_)))

print(re.sub(r"'BOOL': (false)", r"'BOOL': 0", str(text_)))
