
# This program reads through a text file "Romeo.txt" and
# converts every word into an element in a list.
# then sorts the list in order.

filename = raw_input("Enter file name: ")
if filename <1: filename="romeo.txt"
fh = open(filename)
lista = list()  # create an empty list called lista.
for line in fh:
    line = line.rstrip()
    words = line.split()
    print words
    for word in words:
        #print word
        if word in lista: break
        lista.append(word)
print lista
print ""
lista.sort()
print lista



