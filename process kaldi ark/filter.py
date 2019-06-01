#!/usr/bin/env python3
from random import randint
import sys

f = open(sys.argv[1],"r")
dic = {}
l = []
for line in f:
    line = line.rstrip('\n')
    uttid, spkid = line.split(' ',1)
    l.append(uttid)
    #print(spkid)

t = open(sys.argv[2],"r")
for line in t:
    line = line.rstrip('\n')
    uttid, text = line.split(' ',1)
    #print("%s,%s,%s"%(uttid,text,line))
    if uttid in l:
        print(line)
