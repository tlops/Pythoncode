"""
 The pyglatin is a game that takes the first letter of
 a word and puts it at the end of the word with "ay"
 e.g charles = harlescay!!
"""
pyg = 'ay' # a variable

original = raw_input('Enter a word:') # Takes user input

if len(original) > 0 and original.isalpha(): # test for empty text and alphanumeric character

    print original
else:
    print 'empty or invalid entry!!'

word = original.lower() # changes it to lower case
first = word[0] # the first character
new_word = word + first + pyg # writes the word with first xter and 'ay'
new_word = new_word[1:len(new_word)] # prints the word without the first xter

print new_word
