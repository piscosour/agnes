import sys
import subprocess
import cmd
import random
from time import sleep
from cores import Core, core_list

## core_list = ["samantha", "agnes", "vicki", "whisper", "good news", "daniel", "serena", "fiona"]
user_list = ["eduardo"]


class Agnes(cmd.Cmd):
	intro = "My name is Agnes. How can I help you?"
	prompt = "[Agnes]"

	def do_hello(self, arg):
		say(agnes_core.greeting, agnes_core.voice)

	def do_sing(self, song):
		song = load_song()
		for line in song:
			print line
			say(line, agnes_core.voice)


	## Borrowed from THX1138

	def do_confess(self, arg):
		responses = ["hmmmm", "yes?", "ohhhhhhhh!", "that's interesting", "be more specific", "I see", "I understand"]
		confession_mode = True
		response_counter = 0
		response_max = random.randint(4,8)

		say("tell me about your sins. I'm listening", agnes_core.voice)
		print "Microphone activated. Agnes awaiting confession..."
		while confession_mode == True:
			sleep(random.randint(3,8))
			say(responses[random.randint(0,len(responses)-1)], agnes_core.voice)
			response_counter = response_counter + 1
			if response_counter == response_max:
				confession_mode = False
		sleep(4)

		signoff = ["I'm sorry, you're time is up", "It's OK. Everything will be alright. You're with me now", 
				   "Let us be thankful we have commerce", "Buy more", "Buy more now", "And be happy"]

		for element in signoff:
			say(element, agnes_core.voice)


	def do_lol(self, arg):
		say("lol", agnes_core.voice)

	def do_yolo(self, arg):
		say("poyo", agnes_core.voice)

	def do_switch(self, new_core):
		for core in core_list:
			if new_core == core.name:
				set_core(new_core)
		else:
			say(agnes_core.switch, agnes_core.voice)

	def do_show(self, arg):
		if arg == "cores":
			for core in core_list:
				if agnes_core.name == core.name:
					print "[active]",
				print core.name
			say("Are you trying to replace me?", agnes_core.voice)
		elif arg == "core":
			print agnes_core.name

	def do_login(self, username):
		global login_check
		global active_user

		for user in user_list:
			if username == user:
				login_check = True
				active_user = user
				say("It's you again", agnes_core.voice)
		else:
			say("I don't know who that is", agnes_core.voice)

	def do_bye(self, arg):
		say(agnes_core.farewell, agnes_core.voice)
		return True


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


def say(text, core):
	subprocess.call(["say", "-v", core, text])

def load_song():
	with open(r"still_alive.txt", 'r') as lyrics:
		song = lyrics.readlines()
	return song

if __name__ == "__main__":
	agnes_core = core_list[2]
	Agnes().cmdloop()
