#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import re 
import sys

currentPath = os.getcwd()

def docFolder():
	global currentPath
	docu = currentPath + "/doc"	#nymapp is the name we will use when creating the folder.
	if not os.path.exists(docu):	#So if the folder "img" exist:
		os.makedirs(docu)
		print "Folder 'img' created successfully"		#We get a confimation message should this be successful.
	else:
		print "Folder 'doc' already exist, this step is ignored.\n"		#A message if the folder already exist.

def vidFolder():
	global currentPath
	video = currentPath + "/videos"	#nymapp is the name we will use when creating the folder.
	if not os.path.exists(video):	#So if the folder "img" exist:
		os.makedirs(video)
		print "Folder 'videos' created successfully"		#We get a confimation message should this be successful.
	else:
		print "Folder 'vid' already exist, this step is ignored.\n"		#A message if the folder already exist.

def musicFolder():
	global currentPath
	music = currentPath + "/music"	#nymapp is the name we will use when creating the folder.
	if not os.path.exists(music):	#So if the folder "img" exist:
		os.makedirs(music)
		print "Folder 'music' created successfully"		#We get a confimation message should this be successful.
	else:
		print "Folder 'music' already exist, this step is ignored.\n"		#A message if the folder already exist.

def imgFolder():
	global currentPath
	images = currentPath + "/images"	#nymapp is the name we will use when creating the folder.
	if not os.path.exists(images):	#So if the folder "img" exist:
		os.makedirs(images)
		print "Folder 'images' created successfully"		#We get a confimation message should this be successful.
	else:
		print "Folder 'img' already exist, this step is ignored.\n"		#A message if the folder already exist.

def docLoop():
	global currentPath
	docus = currentPath + "/doc"
	filesInDir = os.listdir(currentPath)
	for files in filesInDir:
		print files
		if files.endswith(".txt"):
			print files
			shutil.move(files, docus)				#move to new directory from the old one (current dir)
			print "Successfully moved the files."
		else:
			print "No files found."
def musicLoop():
        global currentPath
        docus = currentPath + "/music"
        filesInDir = os.listdir(currentPath)
        for files in filesInDir:
                print files
                if files.endswith(".mp3"):
                        print files
                        shutil.move(files, docus)                               #move to new directory from the old one (current dir)
                        print "Successfully moved the files."
                else:
                        print "No files found."
def vidLoop():
        global currentPath
        docus = currentPath + "/videos"
        filesInDir = os.listdir(currentPath)
        for files in filesInDir:
                print files
                if files.endswith(".mp4") or files.endswith(".avi"):
                        print files
                        shutil.move(files, docus)                               #move to new directory from the old one (current dir)
                        print "Successfully moved the files."
                else:
                        print "No files found."
def imgLoop():
        global currentPath
        docus = currentPath + "/img"
        filesInDir = os.listdir(currentPath)
        for files in filesInDir:
                print files
                if files.endswith(".jpg") or files.endswith(".png"):
                        print files
                        shutil.move(files, docus)                               #move to new directory from the old one (current dir)
                        print "Successfully moved the files."
                else:
                        print "No files found."


print ('What would you like to do?')
print ('1 - Documents')
print ('2 - Videos')
print ('3 - Music')
print ('4 - Pictures')
print ('5 - Exit')
myChoice = int(input())
if myChoice == 1:
	docFolder()
	docLoop()
if myChoice == 2:
	vidFolder()
	vidLoop()
if myChoice == 3:
	musicFolder()
	musicLoop()	
if myChoice == 4:
	imgFolder()
	imgLoop()
if myChoice == 5:
	exit()
