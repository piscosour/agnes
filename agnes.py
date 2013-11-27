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
import urllib2
# import usb.core
import wikipedia
import time
from fiftyshades import fiftyshades
from cores import Core, core_list
from termcolor import colored
from bs4 import BeautifulSoup
## from watchdog.observers import Observer
## from watchdog.events import FileSystemEventHandler


## core_list = ["samantha", "agnes", "vicki", "whisper", "good news", "daniel", "serena", "fiona"]
## user_list = ["eduardo"]
## active_user = "you"
agnes_core = core_list[2]
dev_names = ["sam", "daniel", "alex", "gladys", "jack"]


## -- Begin AgNES Cmd class definition -- ##

class Agnes(cmd.Cmd):
	intro = "My name is Agnes. How can I help you?"
	prompt = colored("[Agnes]", "blue")

	## Commands, alphabetically sorted

	# Diegetic about

	def do_about(self, arg):
		if check_core("NEUROTICISM") is not True:
			for i in range(5):
				say('I\'m in space')
				time.sleep(random.randint(1,3))
		elif check_core("SOCIABILITY") is not True:
			say('AgNES revision 2 build 45. System functional. Enter status at prompt for detailed information. Maintenance information can be found in facilities office.\nLastest patch applied by user ' + dev_names[random.randint(0,len(dev_names)-1)])
		elif check_core('EMPATHY') is not True:
			say('This is Agnes. Please await further instructions.')
		elif check_core('CURIOSITY') is not True:
			say('Hi, I\'m Agnes. I\'m doing alright. I guess we should hang. Or whatever.')
		elif check_core('DISCIPLINE') is not True:
			say('My name is Agnes, and I will be your companion during your journey. Like those people in The Hobbit. Did they shoot that film in Sweden? Why not try a Holiday in Sweden this year? See the lovely lakes, the wonderful telephone system, and many interesting furry animals. Including the majestic moose. A moose once bit my sister. No really! She was carving her initials on the moose with the sharpened end of an interspace toothbrush given her by Svenge - her brother-in-law - an Oslo dentist and star of many Norwegian movies: "The Hot Hands of an Oslo Dentist", "Fillings of Passion", "The Huge Molars of Horst Nordfink". Mind you, moose bites can be pretty nasty.')
		else:
			say('My name is Agnes, and I will be your companion during your journey. I\'m a result of years of research at the Dunder Mifflin Paper and Aerospace Company around deep space exploration and psychological well being. I can provide you with information, entertainment, and especially with a voice to keep you company during the long, cold nights in space.')

	def do_bye(self, arg):
		say(agnes_core.farewell, agnes_core.voice)
		return True

	## Borrowed from THX1138

	def do_confess(self, arg):
		if check_core('EMPATHY') is True:
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
		else:
			say('I\'m not really interested in your problems')


	def do_hello(self, arg):
		if check_core("SOCIABILITY") is True:
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
		if check_core("NEUROTICISM") is not True:
			say("L O L O L O L")
		else:
			say("I don't really see what's funny", agnes_core.voice)

	def do_open(self, arg):
		return True

	def do_poem(self, arg):
		text = ''
		if check_core('CURIOSITY') is not True:
			req = urllib2.Request("http://www.smalltime.com/Haiku?main=10", headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', "Accept" : "text/html"})
			contents = urllib2.urlopen(req).read()
 
			soup = BeautifulSoup(contents, "html5lib")

			for tag in soup.find_all('strong'):
				for element in tag.children:
					text = text + element.string

		say(text)


	# Deprecated 

	# def do_set(self, setting, value):
	# 	if setting == "master":
	# 		return True

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

	def do_status(self, arg):
		if check_core('NEUROTICISM') is True:
			for core in core_list:
				if core.active == True:
					print core.name + " core is " + colored("ONLINE", "green")
				else:
					print core.name + " core is " + colored("OFFLINE", "red")
		if check_core('NEUROTICISM') is not True:
			req = urllib2.Request("http://www.wisdomofchopra.com/iframe.php", headers={"Accept" : "text/html"})
			contents = urllib2.urlopen(req).read()
			 
			soup = BeautifulSoup(contents, "html5lib")

			h3counter = 0

			for div in soup.find_all(id='quote'):
				say(div.string)

	def do_story(self, arg):
		# Gives narrative content to the user.
		# If Curiosity is turned off, reads a tweet. If Empathy, reads from a changelog.
		if check_core('EMPATHY') is not True:
			say(fiftyshades[random.randint(0,len(fiftyshades)-1)])
		elif check_core('EMPATHY') is True and check_core('DISCIPLINE') is True:
			say('I only know some really nasty stories, and I care enough about you not to tell them')
		elif check_core("DISCIPLINE") is not True and check_core('EMPATHY') is True:
			req = urllib2.Request("http://www.fmylife.com/random", headers={"Accept" : "text/html"})
			contents = urllib2.urlopen(req).read()
			 
			soup = BeautifulSoup(contents, "html5lib")

			h3counter = 0

			for div in soup.find_all('div', class_='post article', limit=1):
				pre_text = ''.join(div.find_all(text=True))
				proc_text = pre_text.split('#')

				say(proc_text[0])


	# def do_switch(self, new_core):
	# 	for core in core_list:
	# 		if new_core == core.name:
	# 			set_core(new_core)
	# 	else:
	# 		say(agnes_core.switch, agnes_core.voice)

	# Extradiegetic about

	def do_thisissometa(self, arg):
		print "##################"
		print "### AgNES v0.3 ###"
		print "##################"
		print "November 2013"
		print "Designed and developed with love for the MIT Media Lab's Science Fiction to Science Fabrication class."

	## Today I Learned: pulls summaries from random Wikipedia articles.
	## If CURIOSITY is active, pulls regular articles - else it pulls from Simple Wikipedia.

	def do_til(self, arg):
		if check_core('DISCIPLINE') is not True:
			req = urllib2.Request("http://hipsteripsum.me/?paras=1&type=hipster-centric", headers={'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', "Accept" : "text/html"})
			contents = urllib2.urlopen(req).read()
 
			soup = BeautifulSoup(contents, "html5lib")

			for div in soup.find_all(id='content'):
				text = div.contents[1].string
		elif check_core("CURIOSITY") is True and check_core('EMPATHY') is True:
			wikipedia.set_lang("en")
			print "english"
			text = wikipedia.summary(wikipedia.random(pages=1))
		elif check_core("CURIOSITY") is not True:
			wikipedia.set_lang("simple")
			print "simple"
			text = wikipedia.summary(wikipedia.random(pages=1))
		elif check_core("CURIOSITY") is True and check_core('EMPATHY') is not True:
			req = urllib2.Request("http://www.elsewhere.org/pomo/", headers={"Accept" : "text/html"})
			contents = urllib2.urlopen(req).read()
 
			soup = BeautifulSoup(contents, "html5lib")

			h3counter = 0
			text = ''
			for div in soup.find_all('div', class_='storycontent'):
				for element in div.contents:
					if element.name == 'h1':
						text = text + element.string + '\n'
					elif element.name == 'h3' and h3counter < 1:
						text = text +  element.string + '\n'
						h3counter = h3counter + 1
					elif element.name == 'h3' and h3counter == 1:
						break
					elif element.name == 'p' and element.string is not None:
						text = text + element.string + '\n'

		question = "Is that interesting " + dev_names[random.randint(0, len(dev_names)-1)] + "?"

		say(text, agnes_core.voice)

		if check_core("CURIOSITY") is not True:
			say(question, agnes_core.voice)

	def do_whois(self, arg):
		if arg not in dev_names:
			say("I don't know who you're talking about")
		elif check_core('DISCIPLINE') is True:
			say("I really shouldn't be talking about this")
		elif check_core('CURIOSITY') is not True:
			say("That's a name I haven't heard of in a while")

	def do_yolo(self, arg):
		if check_core("NEUROTICISM") is not True:
			say("dude, like, totally, right?")
		else:
			say ("I'm not sure I understand what you mean")

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


# Deprecated in new design

# def set_core(core):
# 	global agnes_core
# 	print "Shutting down core " + agnes_core.name + "...",
# 	say("good-bye", agnes_core.voice)
# 	print "SUCCESS."
# 	print "Activating core " + core + "...",
# 	agnes_core = core
# 	say("Hello", agnes_core.voice)
# 	print "SUCCESS."

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
			# time.sleep(0.5)
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
					print "[" + core.name + " core is now " + colored("ONLINE", "green") + "]"
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
			return element.active

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
	print "Initialising Agnes..."
	init_cores()
	## time.sleep(2)

	Agnes().cmdloop()
