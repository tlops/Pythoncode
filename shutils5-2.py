#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

def copy_file():
    src = os.getcwdu() + '/aohf.txt'
    dest = os.getcwdu() + '/neweeex13'
    shutil.copy(src, dest)
    print 'We have copied the file'

def make_tar():
    dest = os.getcwdu() + '/neweeex13/'
    shutil.make_archive('aohf.txt', 'gztar', '.', dest)
    print 'You have created a tar file'

copy_file()
make_tar()
