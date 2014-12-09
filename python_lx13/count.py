#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Falade Olumuyiwa Lx13  Written 12/08/2014

fil = open('svenskaord.txt')
"""cont = 0
fist= 0
for i in fil:
    i = i.rstrip()
    if fist <= 10:
        cont += 1
        print i
        fist += 1

print cont """

lista =[]
count = 0
for lines in fil:
    lines = lines.rstrip()
    lista.append(lines)
    count +=1

print count

count2 = count/2

print lista[count2], count2
print "#"*23
print lista.index('kvalificerade')


def get_info():
    choicelist = []
    wrdlength = input('How long is the word you chose: ')
    for i in range(wrdlength):
        choicelist.append('-')
    for strw in  choicelist:
        print strw,

get_info()



