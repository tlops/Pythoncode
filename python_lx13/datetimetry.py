#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, calendar

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

###################################################
# Extract time info from file
def split_date(logdate):
    year = datetime.date.today()
    year = year.year
    md = logdate[0:6]
    md =md.split()
    month = list(calendar.month_abbr).index(md[0])
    day = md[1]
    hour = logdate[7:9]
    minut = logdate[10:12]
    seconds = logdate[13:15]

    fulltime = datetime.datetime(year, month, int(day), int(hour), int(minut), int(seconds))
    unixtime = calendar.timegm((year, month, int(day), int(hour), int(minut), int(seconds)))

    return fulltime, unixtime
##########################################################3

print split_date("Dec  1 09:38:27")

ad, ac = split_date("Dec  1 09:38:27")
print ("this is the list: {} and this is the unix: {}".format (ad, ac))

#########################################################
# convert to datetime.date and datetime.time

def change_year(year):
    if validate_date(year):
        year_split = year.split("-")
        #print year_split
        split0 = int(year_split[0])
        split1 = int(year_split[1])
        split2 = int(year_split[2])
        new_year = datetime.date(split0, split1, split2)
        return new_year

def change_time(thetime):
    if not validate_date(thetime):
        time_split = thetime.split(":")
        #print time_split
        tsplit0 = int(time_split[0])
        tsplit1 = int(time_split[1])
        tsplit2 = int(time_split[2])
        new_time = datetime.time(tsplit0, tsplit1, tsplit2)
        return new_time

###################################################################

#global
print type(change_year('2014-10-12'))
print change_year('2014-10-12')
print "##"*12
print change_time('14:30:12')
print type(change_time('14:30:12'))

compdat = datetime.datetime.combine(change_year('2014-10-12'),  change_time('14:30:12'))
print compdat

