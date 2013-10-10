class Core:

	'''Definitions and values for personality cores.'''

	def __init__(self, name, voice, politeness, greeting, farewell, switch):
		self.name = name
		self.voice = voice
		self.politness = politeness
		self.greeting = greeting
		self.farewell = farewell
		self.switch = switch


core_list = [

	Core(name="happy",
		 voice="fiona",
		 politeness=5,
		 greeting="Oh my god, you're here! This makes me so happy!",
		 farewell="Oh man! What a bummer! Come back soon!",
		 switch="Oh boy! Sorry to let you down!"),

	Core(name="nice",
		 voice="vicki",
		 politeness=4,
		 greeting="Nice to see you!",
		 farewell="Have a nice day!",
		 switch="Was it something I said?"),

	Core(name="neutral", 
		 voice="samantha",
		 politeness=3,
		 greeting="Hello",
		 farewell="Good-bye!",
		 switch="Are you trying to replace me?"),

	Core(name="rude",
		 voice="serena",
		 politeness=2,
		 greeting="What's up?"
		 farewell="Go away",
		 switch="I didn't want to be here anyway"),

	Core(name="angry",
		 voice="agnes",
		 politeness=1,
		 greeting="What do you want?",
		 farewell="Get the fuck out",
		 switch="Good, get me out of here")

]