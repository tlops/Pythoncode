#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Falade Olumuyiwa Lx13  Written 12/03/2014

from motor import *
# Here we create an object of the HybricMotor class

#car5 = HybridMotor(brand="Audi", colour="Red", temp=6 )

carA= ElectricMotor(brand="Audi -A8", colour ="Red")
print carA.temp
carA.checkInfo()
carA.start()
carA.checkInfo()
print"###### Drive car  #######33"
carA.drive(2, 50)
carA.PowerConsumption()
print " "
carA.checkInfo()

carA.drive(2, 150)
carA.PowerConsumption()
print " "

