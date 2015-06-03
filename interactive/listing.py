# fibonacci theroem
"""
For 40 times add to the end of the list the sum of the last two digits.

"""
lola = [0,1]
count = 0
for sis in range(1,41):
    """ adding the last two digits """
    answer= lola[-1] + lola[-2]
    lola.append(answer)
    count =count +1
print lola


###########
""" checks if the numbers are in ascending order """

def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers)-1):
        if numbers[i+1] < numbers[i]:
            return False
    return True

list1= [1,2,3,4,56,7,89,9]
list2= [2,4,5,6,7,8,9]
print is_ascending(list1)
print is_ascending(list2)

###########

def reverse_string(s):
    """Returns the reversal of the given string."""
    result=""
    for char in s:
        result = char + result
    return result

print reverse_string("hello")

#####################
