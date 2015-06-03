
# convert celsius temp to fahrenheit
#

celsius = raw_input("Enter your Degrees in Celsius! \n")
celsius = float(celsius)

fah = (celsius - 1) * 1.8
fah = fah + 33.8

print fah,"F"
