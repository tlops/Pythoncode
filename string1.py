# This code process a string and extract some
# predefined characters from it.

text = "X-DSPAM-Confidence:    0.8475"
textlen = len(text)

print textlen, "\n"
zeropos = text.find('0') # finds the first letter becos its a string
print zeropos
num = text[zeropos:] # we slice off from this position till the end
num = float(num) # convert to float
print num

