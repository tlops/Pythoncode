#!/usr/bin/python
""" This scritpt reads through a syslog file and does the following:
    0. The filename is specified on the command prompt when the program is launched.
       (Optionally, fall back to some default filename if no filename was
       specified on the command prompt)
    1. Find all lines that contains "application_end" in syslog data
    2. Extract values "origsent", "termsent", "application" from each line
    3. Per "application" found, sum together all "origsent"
    4. Per "application" found, sum together all "termsent"
    5. output  Name, Origsent, Termsent. in that order.
    6. applications found should be sorted in alphabetical order
    7. Name column should be left-justified.
       Origsent and Termsent columns should be right-justified.
    8. Numeric values in Origsent and Termsent columns should be grouped by
       thousands, with a comma between groups.
    9. Each column should be just wide enough to contain all values, but no wider.
   10. Each column should be separated by two whitespace characters (ascii-code 32).

   11. Name        Origsent    Termsent
       brapp       125,112    2,932,621
       dox_bleep   50,992     1,000,022
       Xanadu      4,175,294  13,223,432
"""
# for formating
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

count1 = 0
firstlist=[] # stuffs that we need, application_end origsent termsent and application
secondlist=[] # application_end origsent application

## this handles point 0.
fname = raw_input("Enter the filename: ")
if len(fname) < 1: fname = "syslog.txt"
fhand = open(fname)

################# point 1-6 ##########
for line in fhand:
   line = line.rstrip()
   words = line.split()
   for word in words:
      if word ==[]: continue #avoid empty lines
      if word == "event=application_end" or word[:9] == "origsent=":
         firstlist.append(word)
      elif word[:9] =="termsent=" or word[:12] =="application=":
         firstlist.append(word)
   count1 =count1 +1

print "There are " +str(count1) + " lines in this file. "
#print len(firstlist)

## write the values of firstlist into a file.
#testfile=open("dist.txt", 'w+')
#for item in firstlist:
#   testfile.writelines("%s \n" % item)
#testfile.close

# checking if it contains the right items
#print "event=application_end" in firstlist[:]

## extract the desired Part of the file and creation of secondlist
for post, ele1 in enumerate(firstlist):
    if ele1 =="event=application_end":
        secondlist.append(firstlist[post+1])
        secondlist.append(firstlist[post+2])
        secondlist.append(firstlist[post+3])

# testing
#print len(secondlist)

# Testing: creates another file that lists the desired items
#testfile2=open("dist2.txt", 'w+')
#for item in secondlist:
#   testfile2.writelines("%s \n" % item)
#testfile2.close

# 3. Per "application" found, sum together all "origsent"
# 4. Per "application" found, sum together all "termsent"
# create dictionaries for selecting application
# and add the origsent and term per application
appl_orig=dict()
appl_term=dict()

##  This code gets the application/origsent value
for position1, stuff in enumerate(secondlist):
    if "application=" in stuff:
        app=stuff.split('=') # splits the words to get the application
        application=app[1]
        post_orig=position1 + 1
        orig=secondlist[post_orig]
        origi=orig.split('=')
        orig_sent=origi[1]
        orig_sent=int(orig_sent)
        appl_orig[application]=appl_orig.get(application,0) + orig_sent

##  This code gets the application/termsent value
for position2, stuff in enumerate(secondlist):
    if "application=" in stuff:
        app_again = stuff.split('=') # splits the words to get the application
        applica_tion = app_again[1] # Application
        term_post = position2 + 2 # the termsent is 2 values away from Application
        term = secondlist[term_post] # This stores the value at secondlist[i]
        new_term = term.split('=') # splits it along'=' "origsent" "1223"
        term_sent = new_term[1] # takes the integer part
        term_sent = int(term_sent) # converts it from string to integer
# for every application of the same kind it adds the value of it origterm
        appl_term[applica_tion] = appl_term.get(applica_tion, 0) + term_sent


## To proceed we need to create a tupple, which is a list in a list
new_appl_orig=[] # new empty list
new_appl_term=[] #

for key,value in appl_orig.items():
    new_appl_orig.append((key,value ))

for key1,value1 in appl_term.items():
    new_appl_term.append((key1,value1))

#print new_appl_orig[:]
print ""
#print new_appl_term[:]
#print ""

########### point 7-10  arranged in alphabetical order
new_appl_term.sort(reverse=False)
new_appl_orig.sort(reverse=False)

# create new list to store the Applcation and the
# corresponding values of Termsent and Origsent
Applications=[]
Termsent=[]
Origsent=[]
#femi=new_appl_term
for keys, values in new_appl_orig:
    Origsent.append(values)
for x, y in new_appl_term:
    Applications.append(x)
    Termsent.append(y)

# creates a tupple of three element Application Origsent and Termsent
final = zip(Applications,Origsent,Termsent)

#The final prints
#print "{0:30} {1:40} {2:16}".format( "Application","Origsent","Termsent")
print "Name \t\t \tOrigsent Termsent"
print "-"*47

## this lines does the same as the last 2 lines
# uncomment any of the next two line to print the result on the screen!

#for keys, values,z in final:
#    print "{0:14} {1:>16n} {2:n}".format(keys,values,z)

#for elements in final:
#    print "{0:14} {1:>16n} {2:n}".format(elements[0],elements[1], elements[2])


#### uncomment this point to direct the output to a file.
myprint=open("syslogoutput.txt",'w+')
myprint.write("Name \t\t \t\t\tOrigsent Termsent\n ")
myprint.write("---------------------------------------------------\n")
for elements in final:
    myprint.writelines( "{0:14} {1:>16n} {2:n}\n".format(elements[0],elements[1], elements[2]))
myprint.close()


