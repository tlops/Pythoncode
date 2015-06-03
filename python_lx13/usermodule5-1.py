#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import platform
import getpass
import grp
import operator
#print os.getgroups() #användaren som man är med i
#print os.geteuid() #användar-id
#print getpass.getuser() # namnet på användaren
#print platform.platform() ##oprativsystemet

listi= os.getcwdu() #sökvägen från programmet
z="johanny"
def create_newfolder(foldername):
    global listi, z, d
    d = listi+"/"+z
    if not os.path.exists(d):
        os.mkdir(d, 0755) # skapar mappen och ger rätigheter
        print "the folder is created "
    else:
        print "The folder already exist!"

def rename_folder(newname):
    global listi, z, d #d = sok/vag/johan
    dst = listi+"/"+newname # sökvägen och de ny mnanet på den gamla mappen
    if not os.path.exists(d): # kollar sökvägen och om mappen finns.
        print "PATH Not Existing!"
    else:
        os.rename(d, dst) # byter namnet på mappen
        #if os.listdir(d)=="":
        print "folder ranamed!"
        #else:
         #   print "The folder is not empty"
asd= "neweeex13"

def make_link():
    global listi
    #dest = "/home/tlops/python_lx13/neweeex/mylinka"
    dest = listi+"/neweeex13/mylinka"
    src =  "/dev/null"
    if not os.path.lexists(dest):
        os.symlink(src, dest) # skapar länken
        print "The link is created "
    else:
        print "The link is already existing!"

print 'Username:',getpass.getuser(),'Name-id:',os.getuid()  # namnet på användaren och användar id.
print '#' * 19
groups = os.getgroups() # hämtar alla  grup numrena.
for i in groups: # loopar igenom alla grup numrena
    g = grp.getgrgid(i) # hämtar all information från grup numrena
    print 'Groups:',operator.attrgetter('gr_name')(g) # hämtar grup namnet från g
print '#' * 19
print ' The path:',listi
print '#' *19
folder= os.listdir(listi) # gör en lista på allt som finns i den mappen
for stuffs in folder: # loppar igenom listan folder
    print 'Files:', stuffs # skriver ut listan folder
print '#' * 19
print ' OS:', platform.platform() # visa oprativsystemet


print '#' * 19
create_newfolder(z)
print '#' * 19
rename_folder(asd)
print '#' * 19
make_link()

