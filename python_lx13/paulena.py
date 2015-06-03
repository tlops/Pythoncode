#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Falade Olumuyiwa Lx13  Written 11/28/2014

import os, time, sys, re
from datetime import datetime
from dateutil.parser import parse

#datum = sys.argv[1]
#tid = sys.argv[2]
#tidinter = sys.argv[3]
if os.getuid() != 0:
    print "you need to be root to run this!"
    sys.exit()

if len(sys.argv) < 2:
    print ("WARNING: {} Require minimum of one argument, YYYY-MM-DD".format(sys.argv[0]))
    print ("Usage: {} YYYY-MM-DD HH:MM:SS <1-23>".format(sys.argv[0]))
    sys.exit()

elif len(sys.argv) < 3:
    sys.argv[2] = "12:00:00"
    sys.argv[3] = 12
#    tid = "12:00:00"
#    tidinter = 12
#    sys.exit()

elif len(sys.argv) < 4:
    sys.argv[3] = 12

#    tidinter = 12
#    sys.exit()
else:
    print "WARNING: Too much argument"
    print ("Usage: {} YYYY-MM-DD HH:MM:SS <1-23>".format(sys.argv[0]))
#    sys.exit()

datum = sys.argv[1]
tid = sys.argv[2]
tidinter = sys.argv[3]

print "#"*34
def validate_date(d):
    global datum
    try:
        datetime.strptime(d, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time(t):
    global tid
    try:
        datetime.strptime(t, '%H:%M:%S')
        return True
    except ValueError:
        return False

def validate_intr(i):
    global tidinter
    try:
        datetime.strptime(i, '%H')
        return True
    except ValueError:
        return False

print validate_intr(tidinter)
print validate_date(datum), validate_time(tid)


def read_files():
    syslog = '/var/log/syslog'
    kern = '/var/log/kern.log'
    auth = '/var/log/auth.log'
    try:
        fh_syslog = open(syslog, 'r')
        fh_kern = open(kern, 'r')
        fh_auth = open(auth, 'r')

        for lines1 in fh_syslog:
            sys_line = lines1.rstrip()
            sys_word = sys_line.split()



    except:
        print "One or more of the system files does not exist."




def main ():
    global tidinter, datum, tid
#    sanity_check()
    if validate_date(datum):
        print "Time is corrrect"
    else:
        print "Time is wrong"

main()
