fname =raw_input("Enter the file name: ")
fhand = open(fname)
counts={}   #creating empty dictionary
for line in fhand:
    words = line.split()
    for word in words:
        word = word.lower() # converts to lower case
        counts[word] = counts.get(word,0) + 1

lst = [] # creating empty list
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

for vali, keyi in lst[:5]:
    print keyi, vali
