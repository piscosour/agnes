class Core:

	'''Definitions and values for personality cores.'''

	def __init__(self, name, voice, politeness, greeting):
		self.name = name
		self.voice = voice
		self.politness = politeness
		self.greeting = greeting


core_list = [

	Core(name="happy",
		 voice="good news",
		 politeness=5,
		 greeting="Oh my god, you're here! This makes me so happy!"),

	Core(name="nice",
		 voice="vicki",
		 politeness=4,
		 greeting="Nice to see you!"),

	Core(name="neutral", 
		 voice="samantha",
		 politeness=3,
		 greeting="Hello"),

	Core(name="rude",
		 voice="serena",
		 politeness=2,
		 greeting="What's up?"),

	Core(name="angry",
		 voice="agnes",
		 politeness=1,
		 greeting="What do you want?")

]