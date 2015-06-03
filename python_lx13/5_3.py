#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Falade Olumuyiwa Lx13  Written 12/02/2014
"""
 This script reads through three log files and prints
 out the log report within the time specified as argument
 to this script.
 USAGE: 5_3.py YYYY-MM-DD HH:MM:SS <1-23>
 a minimum of date is required to run the script, then it
 takes 12:00:00 as the default time and 12 as the interval
 to search the log files

"""

import os, sys, time, calendar
import datetime

def split_date(logdate):
#   This function reads through a line and extract the human readable time
#   eg. (Dec 1 12:23:13) and converts it to fultime 2014-12-01 12:23:13 and
#   unix version of the time, which is an integer in seconds.
    year = datetime.date.today()
    year = year.year
    md = logdate[0:6]
    md = md.split()
    month = list(calendar.month_abbr).index(md[0])
    day = md[1]
    hour = logdate[7:9]
    minut = logdate[10:12]
    seconds = logdate[13:15]

    fulltime = datetime.datetime(year, month, int(day), int(hour), int(minut), int(seconds))
    unixtime = calendar.timegm((year, month, int(day), int(hour), int(minut), int(seconds)))
    return fulltime, unixtime


###################################################3
#   The functions defined here checks the argument to make sure they are
#    written in the right format.

#   checks that the date given as argument is in correct format
#   (YYYY-MM-DD) returns true if correct, otherwise it returns false
def validate_date(d):
    try:
        datetime.datetime.strptime(str(d), '%Y-%m-%d')
        return True
    except ValueError:
        return False

#   checks that the time given as argument is in correct format
#   (HH:MM:SS) returns true if correct otherwise it returns false
def validate_time(t):
    try:
        datetime.datetime.strptime(str(t), '%H:%M:%S')
        return True
    except ValueError:
        return False

#   checks that the interval is within the hour range it
#   returns true if correct otherwise it returns false
def validate_interv(i):
    try:
        datetime.datetime.strptime(str(i), '%H')
        return True
    except ValueError:
        return False


################################3
#   The function here converts the date and time format entered as
#   argument (string) to the 'datetime.date' and 'datetime.time'
#   format. It will be useful during combine when we need to get
#   the actual time.
def change_year(years):
    year_split = years.split('-')
    split0 = int(year_split[0])
    split1 = int(year_split[1])
    split2 = int(year_split[2])
    new_year = datetime.date(split0, split1, split2)
    return new_year

def change_time(times):
    time_split = times.split(':')
    tsplit0 = int(time_split[0])
    tsplit1 = int(time_split[1])
    tsplit2 = int(time_split[2])
    new_time = datetime.time(tsplit0, tsplit1, tsplit2)
    return new_time

#####################################################
#   This function handles the argument entered on the command line
#   it ensures that the right amount of argument are entered and it
#   uses the ''

def sanity_check():
    global tidsinterval
    global datum
    global tid
    try:
        datum = sys.argv[1]
    except IndexError:
        print ("WARNING: {} Require minimum of one argument, YYYY-MM-DD".format(sys.argv[0]))
        print ("USAGE: {} YYYY-MM-DD HH:MM:SS <1-23>".format(sys.argv[0]))
        sys.exit()

    try:
        tid = sys.argv[2]
    except IndexError:
        tid = "12:00:00"

    try:
        tidsinterval = sys.argv[3]
    except IndexError:
        tidsinterval = 12

    if validate_date(datum) == False:
        print 'WARNING: Wrong date format YYYY-MM-DD'
        sys.exit(1)
    if validate_time(tid) == False:
        print 'WARNING: Wrong time format HH:MM:SS'
        sys.exit(1)
    if validate_interv(tidsinterval) == False:
        print 'WARNING: Wrong interval form HH <1-23> '
        sys.exit(1)



def main():
    if os.getuid() != 0: # checks to make sure you are root
        # because the files will not open except you are root
        print "You need to be root to run this Script!"
        sys.exit(1) # Exits the system


    sanity_check() # calling the sanity_check function
#   I am not using try/ except because the file path is specified
#   in the code and the user needs to be root to execute this script.

    tsyslog = open('/var/log/syslog', 'r')  # open the files for reading
    tkernlog = open('/var/log/kern.log', 'r')
    tauthlog = open('/var/log/auth.log', 'r')

#   print "WARNING: some files cannot be read due to Priviledges"
#   We put the files and names in a dictionary to make it easy to extract the file that produces the log
    allfiles = { 'syslog':tsyslog.readlines(), 'kernlog':tkernlog.readlines(), 'authLog':tauthlog.readlines()}

#   Here I compute the time so that they can be used by the datetime.timedelta module
#   I used the 'change_year' and 'change_time' to convert the date and time argument
#   to 'datetime.date' and 'datetime.time' format.
    completeDate = datetime.datetime.combine(change_year(datum), change_time(tid) )
#   I used the timedelta function to get the start and stop interval as specified on the
#   commandline.
    startDate = completeDate - datetime.timedelta(hours=int(tidsinterval))
    stopDate = completeDate + datetime.timedelta(hours=int(tidsinterval))
    infoList = [] # an empty list that will be later used to store the right informatio
#   (unixDatum, filename, lines)  the unixdatum is useful for sorting.

    for filename, files in allfiles.items():
#   Reading through the allfiles dictionary to get the filename and readlines
#   for every file you read the lines in them,  parse it through the 'split_date'
#   function to convert the date to datetime.date format and the unixtime.
        for lines in files:
            lines = lines.rstrip()
            fileDate, unixDatum = split_date(lines)
#   The line above stores the two values returned from the 'split_date()' function in
#   fileDate and UnixDatum
#
            if startDate <= fileDate <= stopDate:
#   The line above compares the time in the file with the time specified as interval time
#   if the startdate is less than filedate and less than stopdate. It will only grab the
#   the lines that fulfill this criteria

                infoList.append((unixDatum,filename,lines))
#   we append the unixDatum which is an interger, filename from the dict and the lines read
#   from each files that meet the condition at the "if" statement

    infoList.sort(reverse = False)
#   sort the list using the unixtime interger and then read through the list to print it
#   out.
    for info in infoList:
        print ("{}: {}".format (info[1], info[2]))

################################################
main()


