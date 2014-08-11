
print 'This skrit counts the number of lines...'
filen = raw_input('Enter your file:')
thefile = open(filen)
x = 0
for lines in thefile:
    x = x + 1
print x

