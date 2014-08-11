count = 0
total = 0

while True:
    num = raw_input("Enter your number: ")
    if num == 'done':
        break
    try:
        num = int(num)
        total= total + num


#       print num

    except:
        print 'Invalid Input!'

print "Total is:", total
