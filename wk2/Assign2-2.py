# This program takes in the number of hours and
# calculate the wage based on the hourly rate of
# $2.75/hr

hrs = raw_input("Enter your number of Hours!! \n")
rate = 2.75
hrs = float(hrs) # converts string to float

wage = rate * hrs

print wage, "USD"

