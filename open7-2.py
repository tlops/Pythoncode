# This script takes a file input ('mbox-short.txt') and searches
# for the floating point number. It then calculates the average
# of all the numbers found.

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "This file does not exit:", fname
    exit()

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    colpos = line.find(':') # finds the position of ':'
    num = line[colpos+1:] # we used the index to locate the string
    total =total + float(num) # convert the string to float & sum
    count = count + 1 # this is a counter.

avg = total / count
    #print line
print "\nThe Average spam Confidence is: ", avg
print "Done!"

