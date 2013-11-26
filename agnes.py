####################################################################
##       AgNES - A(u)gmented Narrative Experience Simulator       ##
## A project for the Science Fiction to Science Fabrication class ##
## at the MIT Media Lab, developed by Eduardo Marisca.            ##
##                          Fall 2013                             ##
####################################################################


import sys
import os
import subprocess
import cmd
import random
import usb.core
import wikipedia
import time
from cores import Core, core_list
from termcolor import colored
## from watchdog.observers import Observer
## from watchdog.events import FileSystemEventHandler


## core_list = ["samantha", "agnes", "vicki", "whisper", "good news", "daniel", "serena", "fiona"]
user_list = ["eduardo"]
active_user = "you"

## -- Begin AgNES Cmd class definition -- ##

class Agnes(cmd.Cmd):
	intro = "My name is Agnes. How can I help you?"
	prompt = colored("[Agnes]", "blue")

	## Commands, alphabetically sorted

	def do_bye(self, arg):
		say(agnes_core.farewell, agnes_core.voice)
		return True

	## Borrowed from THX1138

	def do_confess(self, arg):
		responses = ["hmmmm", "yes?", "ohhhhhhhh!", "that's interesting", "be more specific", "I see", "I understand"]
		confession_mode = True
		response_counter = 0
		response_max = random.randint(4,8)

		say("tell me about your sins. I'm listening", agnes_core.voice)
		print "Microphone activated. Agnes awaiting confession..."
		while confession_mode == True:
			time.sleep(random.randint(3,8))
			say(responses[random.randint(0,len(responses)-1)], agnes_core.voice)
			response_counter = response_counter + 1
			if response_counter == response_max:
				confession_mode = False
		time.sleep(4)

		signoff = ["I'm sorry, you're time is up", "It's OK. Everything will be alright. You're with me now", 
				   "Let us be thankful we have commerce", "Buy more", "Buy more now", "And be happy"]

		for element in signoff:
			say(element, agnes_core.voice)

	def do_hello(self, arg):
		say(agnes_core.greeting, agnes_core.voice)

	# def do_login(self, username):
	# 	global login_check
	# 	global active_user

	# 	for user in user_list:
	# 		if username == user:
	# 			login_check = True
	# 			active_user = user
	# 			say("It's you again", agnes_core.voice)
	# 	else:
	# 		say("I don't know who that is", agnes_core.voice)

	def do_lol(self, arg):
		say("lol", agnes_core.voice)

	def do_status(self, arg):
		for core in core_list:
			if core.active == True:
				print core.name + " core is " + colored("ONLINE", "green")
			else:
				print core.name + " core is " + colored("OFFLINE", "red")

	def do_set(self, setting, value):
		if setting == "master":
			return True

	def do_sing(self, song):
		song = load_song()
		for line in song:
			print line
			say(line, agnes_core.voice)

	## These two are deprecated in the new design

	# def do_show(self, arg):
	# 	if arg == "cores":
	# 		for core in core_list:
	# 			if agnes_core.name == core.name:
	# 				print "[active]",
	# 			print core.name
	# 		say("Are you trying to replace me?", agnes_core.voice)
	# 	elif arg == "core":
	# 		print agnes_core.name

	# def do_switch(self, new_core):
	# 	for core in core_list:
	# 		if new_core == core.name:
	# 			set_core(new_core)
	# 	else:
	# 		say(agnes_core.switch, agnes_core.voice)

	def do_thisissometa(self, arg):
		print "###################"
		print "### Agnes v0.2. ###"
		print "###################"
		print "October 2013."
		print "Designed and developed with love for the MIT Media Lab's Science Fiction to Science Fabrication class."

	## Today I Learned: pulls summaries from random Wikipedia articles.
	## If CURIOSITY is active, pulls regular articles - else it pulls from Simple Wikipedia.

	def do_til(self, arg):
		if check_core("curiosity") is True:
			wikipedia.set_lang("en")
		else:
			wikipedia.set_lang("simple")

		text = wikipedia.summary(wikipedia.random(pages=1))

		say(text, agnes_core.voice)

	def do_whois(arg):
		return True

	def do_yolo(self, arg):
		say("poyo", agnes_core.voice)

	## Cmd class commands

	def postcmd(self, stop, line):
		check_cores(core_list)

## -- End AgNES Cmd class definition -- #

## CoreMonitor is a threaded watchdog that handles changes to the /Volumes folder

# class CoreMonitor(FileSystemEventHandler):
#     def __init__(self, observer):
#         self.observer = observer

#     def on_any_event(self, event):
#     	check_cores()


def get_core():
	return True

def set_core(core):
	global agnes_core
	print "Shutting down core " + agnes_core.name + "...",
	say("good-bye", agnes_core.voice)
	print "SUCCESS."
	print "Activating core " + core + "...",
	agnes_core = core
	say("Hello", agnes_core.voice)
	print "SUCCESS."

## For cross-platform functionality, modify the say function below with whatever local parameters you need

def say(text, core=agnes_core.voice):
	subprocess.call(["say", "-v", core, text])

def load_song():
	with open(r"still_alive.txt", 'r') as lyrics:
		song = lyrics.readlines()
	return song

## Scan cores folder for core sources, activate existing ones

def load_cores(core_list=core_list):
	for element in os.listdir("cores"):
		for core in core_list:
			if element == core.name:
				core.active = True

## Loop listens for core presence after ever command

def get_cores():
	volume_list = os.listdir("/Volumes")

	if "Macintosh HD" in volume_list:
		volume_list.remove("Macintosh HD")
	if "MobileBackups" in volume_list:
		volume_list.remove("MobileBackups")

	return volume_list

## Initial core check

def init_cores(core_list=core_list):
	active_cores = get_cores()

	for element in active_cores:
		for core in core_list:		
			if element == core.name:
				if core.active == False:
					core.active = True

	for core in core_list:
		print "Activating " + core.name + " core",
		for i in range(3):
			print ".",
			## time.sleep(1)
		if core.active == True:
			print colored("SUCCESS", "green")
		else:
			print colored("ERROR", "red")

## Ongoing core check

def check_cores(core_list=core_list):
	active_cores = get_cores()

	for core in core_list:
		for element in active_cores:
			if element == core.name:
				if core.active == False:
					print core.name + " core is now ONLINE"
					core.active = True
					break
				else:
					break
		else:
			if core.active == True:
				print colored("[Warning] " + core.name + " core is offline. Please contact technical support.", "red")
			core.active = False

## Check current status for any individual core

def check_core(core):
	for element in core_list:
		if core.upper() == element.name:
			return True
	else:
		return False

# def init_core_monitor():
# 	path = "/Volumes"
# 	observer = Observer()
# 	event_handler = CoreMonitor(observer)
# 	observer.schedule(event_handler, path)
# 	observer.start()
# 	try:
# 	    while True:
# 	        time.sleep(1)
# 	except KeyboardInterrupt:
# 	    observer.stop()
# 	observer.join()

if __name__ == "__main__":
	os.system("clear")
	agnes_core = core_list[2]
	print "Initialising Agnes..."
	init_cores()
	## time.sleep(2)

	Agnes().cmdloop()
