#!/usr/bin/env python
# Python and numpy are required to use this script.

from sys import argv, exit
import numpy as np
import os

filnam="abinit_vars_play.yml"
filnam1="varname_in.yml"
Input= file(filnam,'r')
Input1= file(filnam1,'r')
outfile = open("abinit_vars_out_play.yml", "wb+")

for oline in Input:
  if oline[0:11] not in "    varname":
    outfile.write(oline)
  if oline[0:11] in "    varname":
    for oline1 in Input1:
      if oline1 == oline:
        oline2=Input1.next()
        if oline2[0:15] in "    topic_class":
          outfile.write(oline2)
          oline3=Input1.next()
          outfile.write(oline3)
          outfile.write(oline)
          break
        if oline2[0:10] in "    topics":
          outfile.write(oline2)
          oline3=Input1.next()
          outfile.write(oline3)
          oline3=Input1.next()
          outfile.write(oline3)
          outfile.write(oline)
          break


outfile.close()




