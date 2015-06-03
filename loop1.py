# This script takes input and prints out
# what was typed in, except if it starts
# with "#".

while True:
    try:
        line = raw_input('>')
        if line[0] =='#':
            continue
        if line == 'done':
            break
        print line
    except:
        print 'Type something!'
print 'Done'
