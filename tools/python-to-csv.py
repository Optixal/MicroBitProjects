#!/usr/bin/env python

# Converts from MicroPython's Image code for micro:bit
# to CSV format, which can be used wwith MultiWingSpan's
# animation.exe. Link to MultiWingSpan's program:
# (http://www.multiwingspan.co.uk/micro.php?page=vbanim)

import re

with open('animation-code.txt', 'r') as f:
    for line in f:
        if line.strip()[:5] == 'Image':
            line = line.strip()
            line = re.sub(r'\D+', '', line)
            line = re.sub(r'\s*', ',', line)
            line = line[1:-1]
            print line
