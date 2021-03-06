#!/usr/bin/python
# TODO: find and solve: wrong generation tagtype['uint128'] 10 instead of 1
import re

print('tagtype = {}')
with open("ECTagTypes.abstract") as f:
    for line in f:
        m = re.match(r"EC_TAGTYPE_(?P<type>[A-Z0-9]*) (?P<code>\d)", line)
        if m != None:
            print('tagtype[\''+m.group('type').lower() + '\'] = ' + m.group('code'))