# This program uses tupples and dictionary to search
# through a file "Mbox-short.txt" and check for mail
# received distribution by hours of the day.



fname = raw_input("Enter file name: ")
counts = dict()
time = list()
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip() # removes line space
    words = line.split() # breaks sentences into words
    if words ==[]: continue # checks for empty lines
    if words[0] !='From' : continue # skips lines not stating with "from"
    for word in words:  # looping through each qualified list
        if ':' not in word: continue # 09:14:15 skips lines not in time format
        time.append(word) # adds the qualified words to a list

for hour in time: # looping through the time list
    hour = hour.split(':') # splits each element at ":" and
    hours=hour[0] # stores the first element in hours
    counts[hours]=counts.get(hours,0) + 1 # counting the first element into a dictionary

newtime = list() # a new empty list
for key, value in counts.items(): # taking the key and values in the dictionary
    newcount=(key, value)
    newtime.append(newcount) # adding it into the new list

newtime.sort(reverse=False) # sorting from lowest up
print newtime

for keys, values in newtime: # loopinf through the key and value of
    print keys, values # the new list to print line by line.



