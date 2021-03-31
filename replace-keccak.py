#!/bin/env python

import sys
import re
from web3 import Web3

data = open(sys.argv[1]).read()
rem = re.findall(r'keccak256\("(.*)"\)', data, re.M)
for k, v in map(lambda x: (x, Web3.keccak(text=x).hex()), rem):
    data = data.replace(f'keccak256("{k}");', f'{v}; // keccak256("{k}")')
print(data)
