# This code takes in a file name and read
# the content in uppercase.

fname = raw_input ("Enter file name: ")
fh = open(fname)
for lines in fh:
    print lines.rstrip().upper() # remove the extra space & make upper case

