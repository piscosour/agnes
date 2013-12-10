class Document:

	def __init__(self, name, description):
		self.name = name
		self.description = description


documents = [

	Document(name='pod bay doors',
		     description="I'm afraid I can't let you do that, Dave")

	Document(name='changelog',
		     description="Latest entry signed by user Gordon. I've made some adjustments to Agnes's cores, they were acting kind of strange and refusing to respond to certain commands. She becomes more helpful when you turn of the Discipline core, but other commands begin to act weirdly. Nothing harmful, it's all in good fun. Four hundred and twenty two days in and I feel like we've become good friends, haven't we, Agnes?"),

	Document(name='certificate',
		     description="Latest entry signed by user Jack. We've finished setting up Agnes for the journey, crew will be rotating in and out of stasis for several months and Agnes will be companion to anyone presently awake. We do not expect her own integrity to be compromised from sleep deprivation, of course, and she will be able to provide a sense of continuity to the journey and the crew. It's strange, though, how we've all resorted to calling her a 'she' at the lab. She's become another member of the crew, perhaps the most important one.")

]