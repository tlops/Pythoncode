#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os




def copy_file():
    inpu=raw_input(' Enter your file: ')
    destfolder=raw_input(' Enter your destination folder: ')
    src = os.getcwdu() + "/"+inpu
    dest = os.getcwdu() +"/"+ destfolder
    print src , dest
    shutil.copy(src, dest)
    print 'We have copied the file'

def make_tar():
    inpu=raw_input(' Enter your file: ')
    destfolder=raw_input(' Enter your destination folder: ')
    dest = os.getcwdu() + "/" +  destfolder
    src = shutil.make_archive( inpu, 'gztar', '.')
    shutil.move(src,dest)
    print 'You have created a tar file'

#copy_file()
make_tar()

    
