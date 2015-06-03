#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Falade Olumuyiwa Lx13  Written 12/09/2014
# This script sorts documents in a folder and places
# them in the appropriate folder.


import os
import shutil
import re
import sys

currentPath = os.getcwd() # current working directory

def docFolder():
	global currentPath # current working directory
	docu = currentPath + "/doc"	#doc is the name we will use when creating the folder.
	if not os.path.exists(docu):	#So if the folder "doc" does not  exist:
		os.makedirs(docu)       # create it
		print "Folder 'img' created successfully"	#We get a confimation message should this be successful.
	else:
		print "Folder 'doc' already exist, this step is ignored.\n"	#A message if the folder already exist.

def vidFolder():
	global currentPath # current working directory
	video = currentPath + "/videos"	# videos is the name we will use when creating the folder.
	if not os.path.exists(video):	# So if the folder "videos" does not exist:
		os.makedirs(video)      # create it
		print "Folder 'videos' created successfully"	#We get a confimation message should this be successful.
	else:
		print "Folder 'vid' already exist, this step is ignored.\n"	#A message if the folder already exist.

def musicFolder():
	global currentPath # current working directory
	music = currentPath + "/music"	# music is the name we will use when creating the folder.
	if not os.path.exists(music):	# So if the folder "music"  does exist:
		os.makedirs(music)
		print "Folder 'music' created successfully"	# We get a confimation message should this be successful.
	else:
		print "Folder 'music' already exist, this step is ignored.\n"	# A message if the folder already exist.

def imgFolder():
	global currentPath # current working directory
	images = currentPath + "/images"	# images is the name we will use when creating the folder.
	if not os.path.exists(images):	# So if the folder "images" does not exist:
		os.makedirs(images)     # create it
		print "Folder 'images' created successfully"	# We get a confimation message should this be successful.
	else:
		print "Folder 'img' already exist, this step is ignored.\n"	# A message if the folder already exist.

def docLoop():
	global currentPath # the current working directory
	docus = currentPath + "/doc" # the new folder
	filesInDir = os.listdir(currentPath) # lists all files in current folder
	for files in filesInDir: # loops through all files
		if files.endswith(".txt"): # if the file ends with .txt
			print files
			shutil.move(files, docus) # move the file to the 'doc' folder from the current folder
			print "Successfully moved the files."
		else:
			print "No files found."
def musicLoop():
        global currentPath  # the current working directory
        docus = currentPath + "/music" # the new folder
        filesInDir = os.listdir(currentPath) # lists all files in current folder
        for files in filesInDir:    # loops through all files
                if files.endswith(".mp3"): # if the file ends with .mp3
                        print files         # print it
                        shutil.move(files, docus)       # move the file to the music folder from the current folder
                        print "Successfully moved the files."
                else:
                        print "No files found."
def vidLoop():
        global currentPath # the current working directory
        docus = currentPath + "/videos" # the new folder
        filesInDir = os.listdir(currentPath) # lists all files in current folder
        for files in filesInDir: # loops through all files
                if files.endswith(".mp4") or files.endswith(".avi"): # if the file ends with .mp4 or .avi
                        print files # print it
                        shutil.move(files, docus) # move the fiel to the 'videos' folder from the current folder
                        print "Successfully moved the files."
                else:
                        print "No files found."
def imgLoop():
        global currentPath #  the current working directory
        docus = currentPath + "/images"  # the new folder
        filesInDir = os.listdir(currentPath)
        for files in filesInDir: # loops through all files
                if files.endswith(".jpg") or files.endswith(".png"): # if the file ends with .jpg or .png
                        print files # print it
                        shutil.move(files, docus) # move the file to the 'img' folder from the current folder
                        print "Successfully moved the files."
                else:
                        print "No files found."

def main ():
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
	sys.exit()

if __name__=='__main__':
    main()

