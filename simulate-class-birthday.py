#!/usr/bin/python3

import random

months = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

year = []

acc = 0

for m in months:
    acc += m
    year.append(acc)

typea = 0
typeb = 0

while True:
    mcnt = [0]*12

    for i in range(28):
        bday = random.randint(0, acc-1)
        for j in range(12):
            if bday < year[j]:
                mcnt[j] += 1
                break

    oneinall = True
    for m in mcnt:
        if m == 0:
            oneinall = False
            break
    
    if oneinall:
        typea += 1
    else:
        typeb += 1

    print("{} {} {}".format(typea, typeb, typea/(typea+typeb)))
