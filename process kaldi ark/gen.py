#!/usr/bin/env python3
from random import randint
import sys

f = open(sys.argv[1],"r")
dic = {}
l = []
for line in f:
    line = line.rstrip('\n')
    uttid, spkid = line.split(' ',1)
    dic[uttid] = spkid
    if spkid not in l:
        l.append(spkid)
#    print uttid
#print l
dic_len = len(dic)
for i in dic:
    spkid = dic[i]
    str = spkid + ' '+ i + " target\n"
#    print i
    flag = True
    while(flag):
        index = randint(0,len(l)-1)
#        print("%s, %s, %s",l[index],spkid, flag)
        if l[index] == spkid:
            index = randint(0,len(l)-1)
        else:
            str += l[index] +' '+ i + " nontarget"
            flag = False
    print(str)





