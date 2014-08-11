fname = raw_input("Enter file name: ")
counts = dict()
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip()
    words = line.split()
    if words ==[]: continue
    if words[0] !='From' : continue
    for word in words:
        counts[word]=counts.get(word,0) + 1
        bigcount=None
        bigword=None
        for word,count in counts.items():
            if '@' not in word: continue
            if bigcount is None or count > bigcount:
                 bigword=word
                 bigcount=count
print bigword, bigcount
