#!/usr/bin/env python3

import argparse
import os
import sys

from psptool.pbp import is_pbp, PBP
from psptool.pack import pack_prx
from psptool.prx import encrypt
from psptool.psar import PSAR
from struct import *

size= os.stat(sys.argv[1]).st_size 
in_file = open(sys.argv[1],"rb")
in_file.seek(0x24,0)
data = in_file.read(4)
psar_loc = int.from_bytes(data,"little")
psar_size = size - psar_loc

print('eboot size: ' + str(size))
print('psar location: ' + str(psar_loc))
print('psar_size ' + str(psar_size))

in_file.seek(psar_loc,0)
outbuf = in_file.read(psar_size)
in_file.close()

executable = open(sys.argv[2],"wb")
executable.write(outbuf)
executable.close()

executable2 = open(sys.argv[2],"rb")
testbuf = executable2.read()

psar = PSAR(testbuf)


