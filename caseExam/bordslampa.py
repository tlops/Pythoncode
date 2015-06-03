#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13

class Bordslampa:
	def __init__(self, brand='Philip', energy='60W', typed='light bulb 60W' ):
		self.brand = brand
		self.price = 20
		self.material = "celluloid"
		self.energy = energy
		self.typed = "lightbulb 60W" # or lowenerybulb 15W
		self.running = False # off: The bulb is off
		self.state = True # set that there is a bulb in the lamp
	
	def turnOn(self):
		if self.running == False: # checks if the bulb is Off
			print "Lights on!"
			self.running = True # put the bulb on
		else: # if on
			print "Light Already on!"
		
	def turnOff(self):
		if self.running == True: # checks if the bulb is On
			print "Lights off!"
			self.running = False # put the bulb off
		else: # if off
			print "Light Already off!"
	
	def removeBulb(self):
		if self.running == False: # checks if the Lamp is off
			print "You can Remove the bulb! Bulb is OFF!"
			if self.state == True: # check if there is a bulb in the lamp
				print "Removing Bulb ..."
				self.state = False # set bulb to removed
				print "Bulb Removed!\n"
			else: # if there is no bulb in th lamp
				print "There is NO bulb to remove.\n"
		else: # if bulb not off
			print "You need to turn OFF the LAMP!"

	def replaceBulb(self):
		if self.running == False:
			print "You can Replace the bulb! Bulb is OFF!"
			if self.state == False:
				print "Replacing Bulb ..."
				self.state = True
				print "Bulb Replaced!\n"
			else:
				print "There is Already a bulb in Place."
				print "You need to Remove the present Bulb!\n"
		else:
			print "You need to turn OFF the LAMP!"
	
	def currentState(self):
		print "Brand: ", self.brand
		print "ON/OFF: ", self.running
		print "There is Bulb: ", self.state
		print "Energy Consumption: ", self.energy
		print "Price: ",self.price




