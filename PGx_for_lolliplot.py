#!/usr/bin/env python

import sys
import re

inputVEP = sys.argv[1]
output = sys.argv[2]
k = open(output, 'w')
with open(inputVEP, "r") as f:
	for line in f:
		line = line.strip()
		if not re.match("##", line):
			k.write ("%s\n" % (line))
				
f.close()
k.close()
