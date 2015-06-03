fname = raw_input("Enter file name: ")
count = 0
listas = list()
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip()
    words = line.split()
    if words ==[]: continue
    if words[0] !='From' : continue
    print words[1]
    count= count + 1
print "There were ", count, "lines that starts with From in the box! "

