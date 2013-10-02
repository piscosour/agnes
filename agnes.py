import sys
import subprocess
import cmd

core_list = ["samantha", "zarvox", "agnes", "vicki", "whisper", "good news", "daniel", "serena", "fiona"]

class Agnes(cmd.Cmd):
	intro = "My name is Agnes. How can I help you?"
	prompt = "[Agnes]"

	def do_hello(self, arg):
		say("hello", agnes_core)

	def do_sing(self, song):
		song = load_song()
		for line in song:
			print line
			say(line, agnes_core)

	def do_lol(self, arg):
		say("lol", agnes_core)

	def do_yolo(self, arg):
		say("poyo", agnes_core)

	def do_switch(self, new_core):
		if new_core in core_list:
			set_core(new_core)
		else:
			say("I don't know who that is", agnes_core)

	def do_show(self, arg):
		if arg == "cores":
			for element in core_list:
				print element
			say("Are you trying to replace me?", agnes_core)
		elif arg == "core":
			print agnes_core


	def do_bye(self, arg):
		say("good-bye", agnes_core)
		return True


def get_core():
	return True

def set_core(core):
	global agnes_core
	print "Shutting down core " + agnes_core + "...",
	print "SUCCESS."
	print "Activating core " + core + "...",
	agnes_core = core
	say("Hello", agnes_core)
	print "SUCCESS."


def say(text, core):
	subprocess.call(["say", "-v", core, text])

def load_song():
	with open(r"still_alive.txt", 'r') as lyrics:
		song = lyrics.readlines()
	return song

if __name__ == "__main__":
	agnes_core = "samantha"
	Agnes().cmdloop()
