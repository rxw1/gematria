#!/usr/bin/python3.8

import sys
from abnum import Abnum, greek

g = Abnum(greek)

print(g.value(sys.argv[1]))
