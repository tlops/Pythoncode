#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

def copy_file():
    src_file=raw_input('Enter the file you want to copy: ') # source file name without the preceeding /
    destfolder=raw_input('Enter the destination folder: ') # destination folder without the preceeding /
    src = os.getcwdu() + "/"+src_file # appending effective search path
    dest = os.getcwdu() +"/"+ destfolder # appending effective search path
    #print src , dest
    if os.path.exists(src): #and os.path.exists(dest): # checks if the file exists
        shutil.copy(src, dest)
        print ('OK: copied from %s to %s '% (src,dest))
    else:
        print ('WARNING: Not copied from %s to %s: wrong file or folder! '% (src,dest))

def make_tar():
    src_file = raw_input('Enter the file you want to zip: ') # source file name without the preceeding /
    destfolder = raw_input('Enter your destination folder: ') # destination folder without the preceeding /
    dest = os.getcwdu() + "/" +  destfolder # appending effective search path
    src = shutil.make_archive( src_file, 'gztar', '.') # creating the tar file
    shutil.move(src,dest) # moving it to the destination folder
    print 'You have created a tar file'

copy_file()
make_tar()


