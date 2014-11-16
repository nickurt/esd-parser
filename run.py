#!/usr/bin/python
import sys
from esd import ESDParser

esd = ESDParser()
esd.setEsdName(sys.argv[1])
esd.parse()
print esd.toBuildString()