#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13

# Testing the Bordslampa class

from bordslampa import Bordslampa

bord1 = Bordslampa(brand='Samsung',energy="15W")
bord1.currentState()
print bord1.brand # check the brand
bord1.turnOn()
print "\n"
## try to On it again
bord1.turnOn()

print "Trying to remove bulb when lamp is On!"
bord1.removeBulb()

print "\nTrying to replace bulb when lamp is On!"
bord1.replaceBulb()

print "#"* 23

print "Turn off he LAmp and remove  and replace bulb"
bord1.turnOff() # turn off
bord1.removeBulb() # remove ulb
bord1.replaceBulb() # replacebulb


