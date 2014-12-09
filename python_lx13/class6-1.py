#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Falade Olumuyiwa Lx13  Written 12/03/2014

from motor import *
import pickle

car = Motors()
car2 = Motors(brand='Toyota', colour='Green')
print "#"* 24
print car2.colour
print car2.brand
print car.change_temp(20)
print car.temp
print car.brand
print car.revperMin
car.stop()
car.start()
car.drive(20,10)
car.stop()
car.drive(20,10)

##################
print "#" * 23
print "Electric Car"

car3 = ElectricMotor(brand='Ferrari', colour='Red')
print car3.colour
print car3.brand
car3.stop()
car3.drive(20,50)
car3.checkInfo()
car3.start()
car3.checkInfo()
car3.drive(10, 50)
car3.PowerConsumption()
car3.drive(10, 70)
car3.PowerConsumption()
car3.drive(70, 95)
car3.PowerConsumption()
car3.drive(70, 195)
car3.PowerConsumption()
car3.drive(10, 19)
car3.PowerConsumption()
car3.Recharge()
car3.start()
car3.drive(10, 19)
car3.PowerConsumption()
car3.checkInfo()

######################################
print '#'*23
print "Bensin Car"
car4 = BensinMotor(brand = 'Volvo', colour = 'White')
car4.carInfo()
car4.start()
car4.carInfo()
car4.drive(20, 60)
car4.fuelConsumption()
car4.carInfo()
###############################

try:
    fname = open('6-2.data', 'w')
except IOError:
    print "Cannot Open the file"
pickle.dump(car2, fname)
pickle.dump(car3, fname)
pickle.dump(car4, fname)



