# This program repeatedly prompts the user
# for interger numbers until the user enters
# 'done'. It then prints out the largest and
# smallest numbers, typed.

largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if smallest is None or largest is None:
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    except:
        print 'Invalid input!'

print "\nSmallest is", smallest
print "Largest is", largest

