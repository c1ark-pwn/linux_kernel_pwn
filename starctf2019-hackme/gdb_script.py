# -*- coding: utf-8 -*-

#########################################################################
# File Name: gdb_script.py
# Created on : 2019-10-09 17:46:11
# Author: raycp
# Last Modified: 2019-11-04 06:24:24
# Description: script for debug lkm
#########################################################################

import gdb

ko_name = "./hackme.ko"
ko_base = int(input("%s base: "%(ko_name)), 16)

gdb.execute("target remote 127.0.0.1:1234")
gdb.execute("add-symbol-file %s 0x%x"%(ko_name, ko_base))
#gdb.execute("b")
